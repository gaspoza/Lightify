#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
from resources.client import Client

BRIDGE_IP = '192.168.0.12'


class Lightify():

    def __init__(self, params=None):
        self._commands = {'info', }

        parser = argparse.ArgumentParser()
        parser.add_argument("--bride_ip", help="set the bridge ip address", default=BRIDGE_IP)

        subparsers = parser.add_subparsers(dest="command")
        subparsers.required = True

        parser_info = subparsers.add_parser('info')
        parser_info.add_argument('--type', choices={'light', 'group'})

        self._lights_options = {'on': 'turn_on', 'off': 'turn_off', 'alert': 'alert'}
        parser_lights = subparsers.add_parser('lights')
        parser_lights.add_argument('action', choices=self._lights_options.keys())
        parser_lights.add_argument('--lights_ids', metavar='id', type=int, nargs='+')

        if params is None:
            args = parser.parse_args()
        else:
            args = parser.parse_args(params)

        self._client = Client(args.bride_ip)

        getattr(self, args.command)(args)

    def info(self, args):
        if args.type is None or args.type == 'light':
            lights = self._client.get_lights()
            for light in lights:
                print(light)

        if args.type is None or args.type == 'group':
            groups = self._client.get_groups()
            for group in groups:
                print(group)

    def lights(self, args):
        lights = self._client.get_lights()

        if args.lights_ids is not None:
            lights = [light for light in lights if light.id in args.lights_ids]

        function_name = self._lights_options[args.action]
        getattr(self._client, function_name)(*lights)


if __name__ == '__main__':
    Lightify()

    # Lightify(['--bride_ip', '192.168.0.50', 'info', ])
    # Lightify(['info', ])
    # Lightify(['info', '--type', 'light', ])
    # Lightify(['info', '--type', 'group', ])

    # Lightify(['lights', 'alert', '--lights_ids', '5', ])
