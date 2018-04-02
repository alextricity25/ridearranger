from ridearranger.models.scenario_rule import ScenarioRule
from ridearranger.scenarios.scenario import Scenario
from ridearranger.modifier import Modifier
import pdb

class ScenarioGenerator():

    def __init__(self, scenario_rule, modifiers, drivers, passengers):

        if not isinstance(scenario_rule, ScenarioRule):
            raise Exception("ScenarioGenerator needs ScenarioRule object to work on!")

        self.scenario_rule = scenario_rule
        self.drivers = drivers
        self.passengers = passengers
        self.modifiers = modifiers

        self.source_location_rule = self.scenario_rule.source_location_rule
        self.dest_location_rule = self.scenario_rule.dest_location_rule

    def get_scenario(self):
        # NOTE: When processing this data, keep in mind that only
        # locations that are not 'same' matter. This is because
        # ride arrangements only matter when considering different
        # locations
        scenario_d = {
            'locations' : {
                'src': dict(),
                'dest': dict()
             }
        } # Get set of passenger and drivers src and dest location and build a dictionary with that
        self._populate_locations(scenario_d, 'src', self.source_location_rule)
        self._populate_locations(scenario_d, 'dest', self.dest_location_rule)
        # Make a scenario object
        scenario = Scenario(scenario_d, self.scenario_rule)
        # The modifer class modifies the scenario object to include
        # and exclude drivers or passengers. Modifiers are defined
        # by the user via groupme
        m = Modifier(self.modifiers)
        m.apply_modifiers_to_scenario(scenario)
        return scenario

    def _populate_locations(self, scenario, direction, rule):
        if rule == 'SL':
            scenario['locations'][direction]['same'] = {
                'drivers': self.drivers,
                'passengers': self.passengers
            }
        elif rule  == 'HL':
            for person in self.drivers + self.passengers:
                scenario['locations'][direction][person.location] = {
                    "drivers": [],
                    "passengers": []
                }
            for location in scenario['locations'][direction].keys():
                for person in self.drivers + self.passengers:
                    if person.location == location:
                        if person.is_driver:
                            scenario['locations'][direction][location]['drivers'].append(person)
                        else:
                            scenario['locations'][direction][location]['passengers'].append(person)
