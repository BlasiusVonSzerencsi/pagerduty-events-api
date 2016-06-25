from unittest import TestCase
from unittest.mock import patch

from pagerduty_events_api import PagerdutyIncident


class TestPagerdutyIncident(TestCase):
    def setUp(self):
        super().setUp()
        self.__subject = PagerdutyIncident('my_service_key', 'my_incident_key')

    def test_get_service_key_should_return_the_service_key(self):
        self.assertEqual('my_service_key', self.__subject.get_service_key())

    def test_get_incident_key_should_return_the_incident_key(self):
        self.assertEqual('my_incident_key', self.__subject.get_incident_key())

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_acknowledge_should_make_pagerduty_api_call(self, post):
        post.return_value = {}

        self.__subject.acknowledge()

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'acknowledge',
                                      'incident_key': 'my_incident_key'})

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_resolve_should_make_pagerduty_api_call(self, post):
        post.return_value = {}

        self.__subject.resolve()

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'resolve',
                                      'incident_key': 'my_incident_key'})
