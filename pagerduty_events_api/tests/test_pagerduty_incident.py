from ddt import ddt, data, unpack

from unittest import TestCase
from unittest.mock import patch

from pagerduty_events_api import PagerdutyIncident


@ddt
class TestPagerdutyIncident(TestCase):
    def setUp(self):
        super().setUp()
        self.__subject = PagerdutyIncident('my_service_key', 'my_incident_key')

    def test_get_service_key_should_return_the_service_key(self):
        self.assertEqual('my_service_key', self.__subject.get_service_key())

    def test_get_incident_key_should_return_the_incident_key(self):
        self.assertEqual('my_incident_key', self.__subject.get_incident_key())

    @data('resolve', 'acknowledge')
    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_resolve_acknowledge_should_make_appropriate_pagerduty_api_calls(self, action, post):
        getattr(self.__subject, action)()

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': action,
                                      'incident_key': 'my_incident_key'})

    @data('resolve', 'acknowledge')
    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_resolve_acknowledge_should_append_additional_data_to_the_api_calls(self, action, post):
        getattr(self.__subject, action)({'description': 'some meaningful description'})

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': action,
                                      'incident_key': 'my_incident_key',
                                      'description': 'some meaningful description'})

    @data('resolve', 'acknowledge')
    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_resolve_acknowledge_should_give_precedence_to_the_mandaroty_params(self, action, post):
        getattr(self.__subject, action)({'event_type': 'some_other_event_type',
                                         'details': {'some_key': 'some value'}})

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': action,
                                      'incident_key': 'my_incident_key',
                                      'details': {'some_key': 'some value'}})

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_should_make_appropriate_pagerduty_api_call(self, post):
        self.__subject.trigger('incident description')

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'trigger',
                                      'description': 'incident description',
                                      'incident_key': 'my_incident_key'})

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_should_append_additional_data_to_the_api_call(self, post):
        self.__subject.trigger('incident description', {'details': {'some_key': 'some value'}})

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'trigger',
                                      'description': 'incident description',
                                      'incident_key': 'my_incident_key',
                                      'details': {'some_key': 'some value'}})

    @patch('pagerduty_events_api.pagerduty_rest_client.PagerdutyRestClient.post')
    def test_trigger_additional_params_should_not_override_description(self, post):
        self.__subject.trigger('incident description', {'description': 'some other description'})

        post.assert_called_once_with({'service_key': 'my_service_key',
                                      'event_type': 'trigger',
                                      'description': 'incident description',
                                      'incident_key': 'my_incident_key'})
