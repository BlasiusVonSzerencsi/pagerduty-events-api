import json
import requests

from ddt import ddt, data, unpack

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import Mock

from pagerduty_events_api.pagerduty_rest_client import PagerdutyBadRequestException
from pagerduty_events_api.pagerduty_rest_client import PagerdutyForbiddenException
from pagerduty_events_api.pagerduty_rest_client import PagerdutyServerErrorException
from pagerduty_events_api.pagerduty_rest_client import PagerdutyNotFoundException

from pagerduty_events_api.pagerduty_rest_client import PagerdutyRestClient


@ddt
class TestPagerdutyRestClient(TestCase):
    def setUp(self):
        super().setUp()
        self.__subject = PagerdutyRestClient()

    def test_post_should_make_pagerduty_api_call(self):
        response = Mock(text='{}', status_code=200)
        requests.post = MagicMock(return_value=response)

        self.__subject.post({'some_key': 'some_value',
                             'another_key': 'another_value'})

        requests.post.assert_called_once_with('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                              json.dumps({'some_key': 'some_value',
                                                          'another_key': 'another_value'}))

    def test_post_should_return_the_json_parsed_reponse_text(self):
        response = Mock(text='{"response_key": "response_value"}', status_code=200)
        requests.post = MagicMock(return_value=response)

        result = self.__subject.post({})

        self.assertEqual({'response_key': 'response_value'}, result)

    @data(
        (404, None, PagerdutyNotFoundException),
        (400, {'message': 'Event object is invalid',
               'errors': ['Description is missing or blank']}, PagerdutyBadRequestException),
        (403, None, PagerdutyForbiddenException),
        (543, None, PagerdutyServerErrorException)
    )
    @unpack
    def test_post_should_raise_error_on_various_error_cases(self, status_code, content, expected_exception):
        requests.post = self.__post_with_content(status_code, content)

        with self.assertRaises(expected_exception):
            self.__subject.post({})

    @staticmethod
    def __post_with_content(status_code, response_content=None):
        response = Mock(status_code=status_code,
                        content=json.dumps(response_content))

        return MagicMock(return_value=response)
