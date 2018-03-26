from ridearranger.models.scenario_rule import ScenarioRule
import pdb

class Scenario():

    def __init__(self, scenario, scenario_rule):

        if not isinstance(scenario_rule, ScenarioRule):
            raise Exception("Scneario needs ScenarioRule object to work on!")

        self.scenario = scenario
        self.scenario_rule = scenario_rule

        # Sub scenario, which is the scenario after the 'group_by_rule'
        # has been applied. This essentially means wheather arrangements
        # are made based on source or based on destination locations.
        self.sub_scenario = self.scenario['locations'][self.scenario_rule.\
        group_by_rule]

    def get_locations(self):
        """
        Get's all locations associated with any person in a scenario
        """
        return self.scenario['locations'][self.scenario_rule.group_by_rule].keys()

    def get_passengers_for_location(self, location):
        """
        Get's passengers for a specific location
        """
        l_passengers = []
        for _location, persons in self.sub_scenario.iteritems():
            if _location == location:
                for passenger in persons['passengers']:
                    l_passengers.append(passenger)

        return l_passengers

    def get_drivers_for_location(self, location):
        """
        Get drivers for a specific location
        """
        l_drivers = []
        for _location, persons in self.sub_scenario.iteritems():
            if _location == location:
                for passenger in persons['drivers']:
                    l_drivers.append(passenger)

        return l_drivers

    def get_spots_for_location(self, location):
        num_spots = 0
        for _location, persons in self.sub_scenario.iteritems():
            if location == _location:
                for driver in persons['drivers']:
                    if not driver.car:
                        raise Exception("ERROR! Driver doesn't have a car assigned!")
                    num_spots += driver.car.num_passengers
        return num_spots

    def get_drivers_needed_for_location(self, location):
        """
        Get the number of drivers *needed* for a specific location
        This method chooses the drivers needed based on optimization, not
        availability or a rotation of drivers. This means that it will
        always return the number of drivers needed in a optimized scenario
        with no constraints.
        """
        num_drivers_needed = 0
        for _location, persons in self.sub_scenario.iteritems():
            if location == _location:
                # Checking to see if there are enough drivers in this
                # location
                num_people = len(
                    persons['drivers'] + persons['passengers'])
                num_spots = self.get_spots_for_location(_location) + len(persons['drivers'])
                if num_spots / num_people < 1.0:
                    raise Exception(
                        "Error!, there are not enough drivers in {}". \
                        format(_location))

                # Here the drivers list is sorted based on the number of passenger
                # seats they have in decending order.
                # Passengers are firstly assigned to drivers with the most
                # space, ensuring efficiency when calculating the
                # number of drivers needed
                # This is a optimized deterministic assingment that
                # is only used to calculate the number of drivers
                # needed. They are not official driver-to-passenger
                # assignments
                drivers_sorted = sorted(
                    persons['drivers'],
                    key=lambda x: x.car.num_passengers,
                    reverse = True)
                for driver in drivers_sorted:
                    # If there are no more people to assign, then we are done
                    if num_people == 0:
                        break # Breaks outer loop
                    num_drivers_needed += 1
                    # Exclude the driver
                    num_people -= 1
                    # Try to fit all the people in this car, but if we can't
                    # then we add another driver
                    curr_passengers = driver.car.num_passengers
                    while num_people != 0:
                        if curr_passengers == 0:
                            break
                        else:
                            curr_passengers -= 1
                            num_people -= 1
        return num_drivers_needed

    def switch_to_passenger_for_location(self, driver, location):
        """
        Switches this driver to be a passenger
        """
        for _location, persons in self.sub_scenario.iteritems():
            if _location == location:
                for _driver in persons['drivers']:
                    if _driver == driver:
                        persons['drivers'].remove(driver)
                        persons['passengers'].append(driver)

#TODO: What about creating a ScheduleGenerator? That generates a schedule of drivers and passengers over the period of a few weeks(or how ever many weeks it takes to rotate through all the drivers). Would this need to work off locations? probably.
