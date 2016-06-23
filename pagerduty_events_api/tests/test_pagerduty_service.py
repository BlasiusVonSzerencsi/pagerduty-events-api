from unittest import TestCase
from unittest.mock import patch

from pagerduty_events_api import PagerdutyService
from pagerduty_events_api import PagerdutyIncident


class TestPagerdutyService(TestCase):
    def setUp(self):
        super().setUp()
        self.__subject = PagerdutyService('my_service_key')

    def test_get_service_key_should_return_the_service_key(self):
        self.assertEqual('my_service_key', self.__subject.get_service_key())

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_should_make_pagerduty_api_call(self, post):
        post.return_value = {'incident_key': 'my_incident_key'}

        self.__subject.trigger('some_description')

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'trigger',
                                      'description': 'some_description'})

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_should_return_a_pagerduty_incident(self, post):
        post.return_value = {'incident_key': 'my_incident_key'}

        incident = self.__subject.trigger('some_description')

        self.assertIsInstance(incident, PagerdutyIncident)

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_should_parse_the_api_response(self, post):
        post.return_value = {'incident_key': 'my_incident_key'}

        incident = self.__subject.trigger('some_description')

        self.assertEqual('my_service_key', incident.get_service_key())
        self.assertEqual('my_incident_key', incident.get_incident_key())
