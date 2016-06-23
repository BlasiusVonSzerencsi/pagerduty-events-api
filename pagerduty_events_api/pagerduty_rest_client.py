import json
import requests


class PagerdutyRestClient:
    def post(self, payload):
        response = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                 json.dumps(payload))

        return json.loads(response.text)
