from ridearranger.scenarios.scenario import Scenario
class Modifier():

    def __init__(self, modifiers):
        self.modifiers = modifiers

    def apply_modifiers_to_scenario(self, scenario):
        if not isinstance(scenario, Scenario):
            raise Exception("modify_scenario requires a Scenario object!")
        for person_name in self.modifiers['included']:
            print "ADDING PERSON!!!!"
            scenario.add_passenger(person_name[1:])
        for person_name in self.modifiers['role_removal']:
            scenario.remove_driver_role(person_name[1:])
        for person_name in self.modifiers['excluded']:
            scenario.remove_person(person_name[1:])
        
        
