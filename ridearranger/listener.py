import json
import requests
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models.person import Person
from .models.car import Car
from .models.scenario_rule import ScenarioRule
from ridearranger.line_parser import LineParser
from ridearranger.scenarios.scenario_generator import ScenarioGenerator
import pdb

# This method is invoked by the urls.py module
# then the "/rides" endpoint is hit with a post request
# The GroupMe bot should be set up so that this endpoint
# is configured as a callback URL.
# In otherwords, each time a message is posted to the
# GroupMe group in which the bot resides, a POST request
# will be made to this URL
@csrf_exempt
def get_ride_request(request):
    url = "https://api.groupme.com/v3/bots/post"
    BOT_ID = getattr(settings, "BOT_ID", "Jesus is Lord")
    # The scenario transformer to use for the request
    print "Got request.."
    if request.method == 'POST':
        print "it's a post request..."
        req_body = json.loads(request.body)
        if '#rides' in req_body['text'].lower():
            parser = LineParser(req_body['text'])
            result = parser.get_result()
            #pdb.set_trace()
           
            # Get ready to generate the scenario
            modifiers = result['modifiers']
            scenario_rule = _scenario_lookup(result['scenario_rule'])
            scenario_gen = ScenarioGenerator(
                scenario_rule,
                _get_drivers(),
                _get_passengers())

            # This is the scenario dataset that we can work with
            # It provides information for individuals based on
            # their source and destination location
            print "Generating Scenario..."
            scenario = scenario_gen.get_scenario()
            print scenario

            # We can now pass that scenario dataset to the modifer plugin,
            # which will further transform it to account for any modifers
            # the user might have provided.
            # TODO: implement modifer plugin


            # After being passed through the modifier plugin, we can now
            # process the dataset and arrange it to form groups of
            # 1 driver plus n number of passengers
            # TODO: implement arranger plugin(s)

#            res_data = {
#                'text': "Welcome to the Ride Arranger Bot(RAB). This app is under development",
#                'bot_id': BOT_ID
#            }

#            r = requests.post(url, json = res_data)
    return HttpResponse("Welcome to Ride Arranger Bot!")


def _get_passengers():
    # Returns list of Person objects that are passengers(not drivers)
    return [person for person in Person.objects.all() if not person.is_driver]

def _get_drivers():
    # Returns list of Person objects that are drivers
    return [person for person in Person.objects.all() if person.is_driver]
            
def _scenario_lookup(scenario_name):
    for scenario in ScenarioRule.objects.all():
        if scenario.name == scenario_name:
            return scenario
