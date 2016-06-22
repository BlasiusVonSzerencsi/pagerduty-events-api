import json
import requests


class PagerdutyService:
    def __init__(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def trigger(self, description):
        payload = {'service_key': self.__key,
                   'event_type': 'trigger',
                   'description': description}

        requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      json.dumps(payload))
