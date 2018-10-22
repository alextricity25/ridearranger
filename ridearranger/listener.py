import json
import requests
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models.person import Person
from .models.car import Car
from .models.scenario_rule import ScenarioRule
from ridearranger.line_parser import LineParser
from ridearranger.scenarios.scenario_generator import ScenarioGenerator
from ridearranger.arrangers.rand import RandomArranger
import pdb
import pprint

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
           
            # Get ready to generate the scenario
            modifiers = result['modifiers']
            scenario_rule = _scenario_lookup(result['scenario_rule'])
            #pdb.set_trace()
            scenario_gen = ScenarioGenerator(
                scenario_rule,
                modifiers,
                _get_drivers(),
                _get_passengers())
            print modifiers
            # This is the scenario dataset that we can work with
            print "Generating Scenario..."
            scenario = scenario_gen.get_scenario()
            # The arranger needs the scenario and scenario rule objects
            #arranger = Arranger(scenario, scenario_rule)

            # After being passed through the modifier plugin, we can now
            # process the dataset and arrange it to form groups of
            # 1 driver plus n number of passengers
            # TODO: implement arranger plugin(s)
            arranger = RandomArranger(scenario, scenario_rule)
            arrangements = arranger.get_arrangements()
            #output = pprint.pformat(arrangements)
            print _output_arrangements(arrangements)
            res_data = {
                'text': _output_arrangements(arrangements),
                'bot_id': BOT_ID
            }

            #r = requests.post(url, json = res_data)
            response = HttpResponse(json.dumps(arrangements), content_type="application/json")
            response['Access-Control-Allow-Origin'] = "*"
            response['Access-Control-Allow-Methods'] = "POST, OPTIONS, GET"
            response['Access-Control-Allow-Headers'] = "content-type"
            response['Access-Control-Max-Age'] = "1000"
            return response

    response = HttpResponse("Welcome to Ride Arranger Bot!")
    
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "POST, OPTIONS, GET"
    response['Access-Control-Allow-Headers'] = "content-type"
    response['Access-Control-Max-Age'] = "1000"
    return response


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

def _output_arrangements(arrangements):
    output_string = ""
    for location, drivers in arrangements.iteritems():
        if location != 'same':
            output_string += "-> " + location + "\n"
        for driver, passengers in drivers.iteritems():
            output_string += "    -> " + driver + "\n"
            for passenger in passengers:
                output_string += "            " + passenger + "\n"
    return output_string

def _serialize_arrangements(arrangements):
    for location, drivers in arrangements.iteritems():
        for driver, passengers in drivers.iteritems():
            for passenger in passengers:
                passenger = model_to_dict(passenger)
