class PagerdutyIncident:
    def __init__(self, service_key, incident_key):
        self.__service_key = service_key
        self.__incident_key = incident_key

    def get_service_key(self):
        return self.__service_key

    def get_incident_key(self):
        return self.__incident_key
