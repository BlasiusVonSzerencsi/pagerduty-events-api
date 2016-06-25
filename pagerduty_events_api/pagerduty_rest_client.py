import json
import requests


class PagerdutyException(Exception):
    pass


class PagerdutyBadRequestException(PagerdutyException):
    pass


class PagerdutyNotFoundException(PagerdutyException):
    pass


class PagerdutyRestClient:
    def post(self, payload):
        response = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                 json.dumps(payload))

        if response.status_code == 400:
            error_content = json.loads(response.content)
            raise PagerdutyBadRequestException(error_content['message'])

        if response.status_code == 404:
            raise PagerdutyNotFoundException('Could not find PagerDuty endpoint.')

        return json.loads(response.text)
