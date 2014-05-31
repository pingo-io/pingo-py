"""Blink an LED

This script assumes:

- ``board.pins[13]`` is a ``DigitalPin``
- there is an LED attached to it

"""

import time
import pingo

board = pingo.detect.MyBoard()
led = board.pins[13]
led.mode = pingo.OUT

while True:
    led.toggle()
    time.sleep(.1)
