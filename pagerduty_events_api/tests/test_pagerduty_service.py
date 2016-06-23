import json
import requests

from unittest import TestCase
from unittest.mock import MagicMock

from pagerduty_events_api import PagerdutyService


class TestPagerdutyService(TestCase):
    def test_get_service_key_should_return_the_service_key(self):
        subject = PagerdutyService('my_service_key')

        self.assertEqual('my_service_key', subject.get_service_key())

    def test_trigger_should_make_pagerduty_api_call(self):
        requests.post = MagicMock()

        PagerdutyService('my_service_key').trigger('some_description')

        requests.post.assert_called_once_with('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                              json.dumps({'service_key': 'my_service_key',
                                                          'event_type': 'trigger',
                                                          'description': 'some_description'}))
