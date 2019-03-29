#!/usr/bin/python3
# -*- coding: utf-8 -*-

from resources.client import Client

GROUP_NAME = 'Living room'

bridge_ip = '192.168.0.12'
client = Client(bridge_ip)

groups = client.get_groups()

groups = [group for group in groups if group.name == GROUP_NAME]

assert(len(groups) == 1)

group = groups[0]
lights = [light for light in group.lights if light.on]

if lights:
    client.alert(*lights)
