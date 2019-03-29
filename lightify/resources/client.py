from resources.phuehandler import PHueHandler


class Client:

    def __init__(self, bridge_ip):
        self._phue_handler = PHueHandler(bridge_ip)

    def get_lights(self):
        return self._phue_handler.get_lights()

    def get_groups(self):
        return self._phue_handler.get_groups()

    def turn_on(self, *lights):
        self._phue_handler.turn_on(*lights)

    def turn_off(self, *lights):
        self._phue_handler.turn_off(*lights)

    def alert(self, *lights):
        self._phue_handler.alert(2, *lights)
