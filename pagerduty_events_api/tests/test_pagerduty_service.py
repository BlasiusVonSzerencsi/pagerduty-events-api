import json
import requests

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import Mock

from pagerduty_events_api import PagerdutyService
from pagerduty_events_api import PagerdutyIncident


class TestPagerdutyService(TestCase):
    def test_get_service_key_should_return_the_service_key(self):
        subject = PagerdutyService('my_service_key')

        self.assertEqual('my_service_key', subject.get_service_key())

    def test_trigger_should_make_pagerduty_api_call(self):
        response = Mock(text='{"incident_key": "my_incident_key"}')
        requests.post = MagicMock(return_value=response)

        PagerdutyService('my_service_key').trigger('some_description')

        requests.post.assert_called_once_with('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                                              json.dumps({'service_key': 'my_service_key',
                                                          'event_type': 'trigger',
                                                          'description': 'some_description'}))

    def test_trigger_should_return_a_pagerduty_incident(self):
        response = Mock(text='{"incident_key": "my_incident_key"}')
        requests.post = MagicMock(return_value=response)

        incident = PagerdutyService('my_service_key').trigger('some_description')

        self.assertIsInstance(incident, PagerdutyIncident)

    def test_trigger_should_parse_the_api_response(self):
        response = Mock(text='{"incident_key": "my_incident_key"}')
        requests.post = MagicMock(return_value=response)

        incident = PagerdutyService('my_service_key').trigger('some_description')

        self.assertEqual('my_service_key', incident.get_service_key())
        self.assertEqual('my_incident_key', incident.get_incident_key())
