import json
import requests

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import Mock

from pagerduty_events_api.pagerduty_rest_client import PagerdutyRestClient


class TestPagerdutyRestClient(TestCase):
    def setUp(self):
        super().setUp()
        self.__subject = PagerdutyRestClient()

    def test_trigger_should_make_pagerduty_api_call(self):
        response = Mock(text='{}')
        requests.post = MagicMock(return_value=response)

        self.__subject.post({'some_key': 'some_value',
                             'another_key': 'another_value'})

        requests.post.assert_called_once_with('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                              json.dumps({'some_key': 'some_value',
                                                          'another_key': 'another_value'}))

    def test_trigger_should_return_the_json_parsed_reponse_text(self):
        response = Mock(text='{"response_key": "response_value"}')
        requests.post = MagicMock(return_value=response)

        result = self.__subject.post({})

        self.assertEqual({'response_key': 'response_value'}, result)
