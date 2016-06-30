.. image:: https://travis-ci.org/BlasiusVonSzerencsi/pagerduty-events-api.svg?branch=master
    :target: https://travis-ci.org/BlasiusVonSzerencsi/pagerduty-events-api

.. image:: https://codeclimate.com/github/BlasiusVonSzerencsi/pagerduty-events-api/badges/gpa.svg
    :target: https://codeclimate.com/github/BlasiusVonSzerencsi/pagerduty-events-api
    :alt: Code Climate

.. image:: https://badge.fury.io/py/pagerduty-events-api.svg
    :target: https://badge.fury.io/py/pagerduty-events-api

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
--------------------

::

    import pagerduty_events_api

    service = pagerduty_events_api.PagerdutyService('my_service_key_123')
    incident = service.trigger('some_alert_description')

..

    Please note, that the trigger method of a pagerduty_events_api.PagerdutyService object returns a pagerduty_events_api.PagerdutyIncident instance. Through this instance You can retrieve the identifier of the triggered incident, acknowledge or resolve it later.

::

    incident.get_service_key()
    incident.get_incident_key()

..

    You may also provide additional information to the triggered incident. For further information please visit the `PagerDuty documentation on triggering incidents
    <https://developer.pagerduty.com/documentation/integration/events/trigger>`_.

::

    incident = service.trigger('some_alert_description', {'client': 'my_very_special_pagerduty_client'})

Acknowledging an incident:
--------------------------

::

    import pagerduty_events_api

    incident = pagerduty_events_api.PagerdutyIncident('my_service_key_123', 'my_incident_key456')
    incident.acknowledge()

..

    Similarly to triggering, You may provide additional data when acknowledging an incident. For further information please visit the `PagerDuty documentation on acknowledging incidents
    <https://developer.pagerduty.com/documentation/integration/events/acknowledge>`_.

::

    incident.acknowledge({'description': 'we are working on it...'})

Resolving an incident:
----------------------

::

    import pagerduty_events_api

    incident = pagerduty_events_api.PagerdutyIncident('my_service_key_123', 'my_incident_key456')
    incident.resolve()

..

    As seen before in acknowledging, You may provide additional data when acknowledging an incident. For further information please visit the `PagerDuty documentation on resolving incidents
    <https://developer.pagerduty.com/documentation/integration/events/resolve>`_.

::

    incident.resolve({'description': 'problem fixed ;-)'})

Thrown exceptions:
------------------

- **pagerduty_events_api.PagerdutyBadRequestException** indicates that the sent request contained a malformed payload
- **pagerduty_events_api.PagerdutyForbiddenException** indicates that the rate limit of the PagerDuty API was reached and the request was denied
- **pagerduty_events_api.PagerdutyNotFoundException** indicates that the PagerDuty events API could not be found, maybe due to DNS error or a breaking change of the API endpoint
- **pagerduty_events_api.PagerdutyServerErrorException** indicates a processing error on the PagerDuty servers
