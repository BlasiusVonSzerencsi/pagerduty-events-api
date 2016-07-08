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

    @patch('pagerduty_events_api.pagerduty_incident.PagerdutyIncident.trigger')
    def test_trigger_should_return_an_incident_instance(self, trigger):
        self.assertIsInstance(
            self.__subject.trigger('some_description'),
            PagerdutyIncident
        )

    @patch('pagerduty_events_api.pagerduty_incident.PagerdutyIncident.trigger')
    def test_trigger_should_trigger_the_incident(self, trigger):
        self.__subject.trigger('some_description')
        trigger.assert_called_once_with('some_description', {})

    @patch('pagerduty_events_api.pagerduty_incident.PagerdutyIncident.trigger')
    def test_trigger_should_pass_the_provided_params_to_the_incident_trigger(self, trigger):
        self.__subject.trigger('some_description', {'details': {'some_key': 'some value'}})
        trigger.assert_called_once_with('some_description', {'details': {'some_key': 'some value'}})
