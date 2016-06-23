import json
import requests

from pagerduty_events_api.pagerduty_incident import PagerdutyIncident


class PagerdutyService:
    def __init__(self, key):
        self.__service_key = key

    def get_service_key(self):
        return self.__service_key

    def trigger(self, description):
        payload = {'service_key': self.__service_key,
                   'event_type': 'trigger',
                   'description': description}

        response = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                 json.dumps(payload))

        incident_data = json.loads(response.text)

        return PagerdutyIncident(self.__service_key, incident_data['incident_key'])
