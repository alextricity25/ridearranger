from ridearranger.models.scenario import Scenario

class ScenarioTransformer():

    def __init__(self, scenario, source_location_rule = home_location,
                 dest_location_rule = same_location):

        if scenario not isinstance(Scenario):
            raise Exception("ScenarioTransformer needs scenario object to work on!")
        self.source_location_rule_choices = [
            "same_location",
            "home_location"]
        self.dest_location_rule_choices = [
            "same_location",
            "home_locations"]

        pass
