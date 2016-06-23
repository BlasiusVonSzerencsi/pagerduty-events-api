from unittest import TestCase

from pagerduty_events_api import PagerdutyIncident


class TestPagerdutyIncident(TestCase):
    def test_get_service_key_should_return_the_service_key(self):
        subject = PagerdutyIncident('my_service_key', 'my_incident_key')

        self.assertEqual('my_service_key', subject.get_service_key())

    def test_get_incident_key_should_return_the_incident_key(self):
        subject = PagerdutyIncident('my_service_key', 'my_incident_key')

        self.assertEqual('my_incident_key', subject.get_incident_key())
