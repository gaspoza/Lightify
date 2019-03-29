#!/usr/bin/python

import json
import time
from phue import Bridge


bridge_ip = '192.168.0.12'
b = Bridge(bridge_ip)

b.connect()

# print(json.dumps(b.get_api(), sort_keys=True, indent=4))

# lights = b.lights

# for l in lights:
#     print(l.name)

# for l in lights:
#     l.on = False

b.set_light([1, 2, 3], 'bri', 10, transitiontime=20)
time.sleep(1)
b.set_light([1, 2, 3], 'bri', 254, transitiontime=20)
time.sleep(1)
b.set_light([1, 2, 3], 'bri', 10, transitiontime=20)
time.sleep(1)
b.set_light([1, 2, 3], 'bri', 254, transitiontime=20)
