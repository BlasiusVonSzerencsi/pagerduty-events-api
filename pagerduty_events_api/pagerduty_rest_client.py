import json
import requests


class PagerdutyNotFoundException(Exception):
    pass


class PagerdutyRestClient:
    def post(self, payload):
        response = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                 json.dumps(payload))

        if response.status_code == 404:
            raise PagerdutyNotFoundException('Could not find PagerDuty endpoint.')

        return json.loads(response.text)
