.. image:: https://travis-ci.org/BlasiusVonSzerencsi/pagerduty-events-api.svg?branch=master
    :target: https://travis-ci.org/BlasiusVonSzerencsi/pagerduty-events-api

.. image:: https://codeclimate.com/github/BlasiusVonSzerencsi/pagerduty-events-api/badges/gpa.svg
    :target: https://codeclimate.com/github/BlasiusVonSzerencsi/pagerduty-events-api
    :alt: Code Climate

====================
PagerDuty Events API
====================

Python wrapper for PagerDuty's Events API.

Installation
============

``pip install pagerduty_events_api``

Examples
========

Triggering an alert:

::

    import pagerduty_events_api

    service = pagerduty_events_api.PagerdutyService('my_service_key_123')
    service.trigger('some_alert_description')