import json
import requests
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models.person import Person
from .models.car import Car

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
    if request.method == 'POST':
        req_body = json.loads(request.body)
        if '#rides' is req_body['text'].lower().encode():
            res_data = {
                'text': "Welcome to the Ride Arranger Bot(RAB). This app is under development",
                'bot_id': BOT_ID
            }

            # There should be a Default Scenario
            # created by now
            #scenario_name = "Default"
            # Import scenario
            #from ridearranger.scenario.scenario import ScenarioTransformer
            # TODO Implement get_scenario_obj
            #scenario_obj = _get_scenario_obj(scenario_name)
            #scenario_transformer = ScenarioTransfomer(scenario_obj)
            # TODO:
            # Scenario transformer needs:
            # 1) A Scenario Model Object
            # 2) List of drivers
            # 3) List of Passengers
            # 4) Each person's source and
            #    dest location
            # This is actually more of a scenario "generator"
            # The "scenario" model should be re-named to "scenario rules".
            r = requests.post(url, json = res_data)

        if '#rides list-drivers' in req_body['text'].lower():
            drivers = []
            for person in Person.objects.all():
                if person.is_driver:
                    drivers.append(person.first_name)

            res_data = {
                'text': '\n'.join(drivers),
                'bot_id': BOT_ID
            }
            r = requests.post(url, json = res_data)
        if '#rides list-passengers' in req_body['text'].lower():
            res_data = {
                'text': '\n'.join(_get_passengers()),
                'bot_id': BOT_ID
            }
            r = requests.post(url, json = res_data)
    return HttpResponse("Welcome to Ride Arranger Bot!")


def _get_passengers():
    return [person.first_name for person in Person.objects.all() if not person.is_driver]
            
