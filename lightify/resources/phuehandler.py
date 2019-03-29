#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from phue import Bridge
from .light import Light
from .group import Group


class PHueHandler:
    """
    PHueHandler is the class handling the communication with the restfull API via phue library.
    """

    def __init__(self, bridge_ip='192.168.0.12'):
        self._bridge = Bridge(bridge_ip)
        self._bridge.connect()

        self._turn_on_command = {'on': True, }
        self._turn_off_command = {'on': False, }
        self._start_alert_command = {'alert': 'lselect', }
        self._stop_alert_command = {'alert': 'none', }

    def get_lights(self):
        lights = self._bridge.lights
        return list(map(create_light, lights))

    def get_groups(self):
        groups = self._bridge.groups
        return list(map(create_group, groups))

    def turn_on(self, *lights):
        for light in lights:
            self._bridge.set_light(light.id, self._turn_on_command)

    def turn_off(self, *lights):
        for light in lights:
            self._bridge.set_light(light.id, self._turn_off_command)

    def alert(self, duration=2, *lights):
        for light in lights:
            self._bridge.set_light(light.id, self._start_alert_command)

        time.sleep(duration)

        for light in lights:
            self._bridge.set_light(light.id, self._stop_alert_command)


def create_light(light):
    light_id = light.light_id
    name = light.name
    light_type = light.type
    brightness = light.brightness
    hue = light.hue
    saturation = light.saturation
    state = light.on
    reachable = light.reachable

    return Light(light_id, name, light_type, brightness, hue, saturation, state, reachable)


def create_group(group):
    group_id = group.group_id
    name = group.name
    on = group.on
    lights = list(map(create_light, group.lights))

    return Group(group_id, name, on, lights)
