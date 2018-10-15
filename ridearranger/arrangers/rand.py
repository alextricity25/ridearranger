import random
from ridearranger.scenarios.scenario import Scenario
from collections import OrderedDict
import pdb


class RandomArranger():
    """
    A loosly randomized plugin that uses serveral conditions as constraints.
    Constraints include:
    1) Optimized space - if randomizing drivers comprimises the ability to
       optimize space, then a different path is chosen to favor optimal
       space effeciency.
    2) ...
    3) ...
    """

    def __init__(self, scenario, scenario_rule):
        self.scenario = scenario
        self.scenario_rule = scenario_rule

    def get_arrangements(self):
        arrangements = dict()
        group_by = self.scenario_rule.group_by_rule
        for location in self.scenario.get_locations():
            drivers = []
            # TODO: Implement _get_drivers_needed
            drivers_needed = self.scenario.get_drivers_needed_for_location(location)
            # Drivers needed should be less then number of available drivers
            if drivers_needed > len(self.scenario.get_drivers_for_location(location)):
                raise Exception("Not enough drivers in area {}".format(location))
            # A list of drivers with the same number of passenger spaces
            # available. This list can be safely randomized
            drivers_with_pass = dict()
            # A dictionary of divers keyed by how many passengers spots they
            # have
            # Initialize the dictionary
            for driver in self.scenario.get_drivers_for_location(location):
                drivers_with_pass[driver.car.num_passengers] = []
            for driver in self.scenario.get_drivers_for_location(location):
                drivers_with_pass[driver.car.num_passengers].append(driver)
            # Sort the dictionary by key, in ascending order
            sorted_drivers =  OrderedDict(sorted(
                drivers_with_pass.items(),
                key=lambda t: t[0],
                reverse = True))
            # Pick the drivers for this location firstly based on how many
            # spots they have, then based on randomness
            for num_pass, _drivers in sorted_drivers.iteritems():
                while _drivers and drivers_needed != 0:
                    index = random.randint(0, len(_drivers) - 1)
                    drivers.append(_drivers.pop(index))
                    drivers_needed -= 1
                if drivers_needed == 0:
                    # Covert remaining drivers to passengers
                    for _driver in _drivers:
                        self.scenario.switch_to_passenger_for_location(_driver, location)


            # Initialize the arrangements dictionary
            arrangements[location] = {}
            for driver in drivers:
                arrangements[location][driver.first_name] = []

            passengers = self.scenario.get_passengers_for_location(location)
            count = 1
            while passengers:
                rand_index = random.randint(0, len(passengers) -1)
                driver_index = (count % len(drivers))
                arrangements[location][drivers[driver_index].first_name].append(passengers.pop(rand_index).first_name)
                count += 1
        return arrangements
            # The rest of the drivers need to be converted to passengers
            #for person in persons['drivers']:
                #persons['drivers'].remove(person)
                #persons['passengers'].append(person)
            # Build arrangement for drivers
            #pass_added = 0
            #for driver in drivers:
                # If the number of passengers added to the driver's vehical
                # is equal the number of passengers they can fit, then
                # we are done and can move on to the next driver
                # Choose a random passenger until driver can fit no more
                # passengers
                #while pass_added != driver.num_passengers:
                    #TODO: Implement
     
                
            # Each driver needs a group of passengers
            #TODO Group each passenger with a driver in this 'location'

