import json
import requests


class PagerdutyIncident:
    def __init__(self, service_key, incident_key):
        self.__service_key = service_key
        self.__incident_key = incident_key

    def get_service_key(self):
        return self.__service_key

    def get_incident_key(self):
        return self.__incident_key

    def acknowledge(self):
        payload = {'service_key': self.__service_key,
                   'event_type': 'acknowledge',
                   'incident_key': self.__incident_key}

        requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      json.dumps(payload))
