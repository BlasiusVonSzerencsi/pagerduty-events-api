from unittest import TestCase

from pagerduty_events_api import PagerdutyService


class TestPagerduty(TestCase):
    def test_get_key_should_return_the_service_key(self):
        subject = PagerdutyService('my_service_key')

        self.assertEqual('my_service_key', subject.get_key())
