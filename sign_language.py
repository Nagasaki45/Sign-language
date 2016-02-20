#!/usr/bin/env python

"""
Entry point for running the project

Spawn two processes: a LeapMotion to WekiMini script and a OSC / Web server
that handle the rest of the back and forth communication.
"""

from multiprocessing import Process
import time

import leap_to_weki
import server

Process(target=leap_to_weki.main).start()
Process(target=server.main).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
