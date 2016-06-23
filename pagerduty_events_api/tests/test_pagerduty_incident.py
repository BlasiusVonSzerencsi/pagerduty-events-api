import json
import requests

from unittest import TestCase
from unittest.mock import MagicMock

from pagerduty_events_api import PagerdutyIncident


class TestPagerdutyIncident(TestCase):
    def test_get_service_key_should_return_the_service_key(self):
        subject = PagerdutyIncident('my_service_key', 'my_incident_key')

        self.assertEqual('my_service_key', subject.get_service_key())

    def test_get_incident_key_should_return_the_incident_key(self):
        subject = PagerdutyIncident('my_service_key', 'my_incident_key')

        self.assertEqual('my_incident_key', subject.get_incident_key())

    def test_acknowledge_should_make_pagerduty_api_call(self):
        requests.post = MagicMock()

        PagerdutyIncident('my_service_key', 'my_incident_key').acknowledge()

        requests.post.assert_called_once_with('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                              json.dumps({'service_key': 'my_service_key',
                                                          'event_type': 'acknowledge',
                                                          'incident_key': 'my_incident_key'}))
