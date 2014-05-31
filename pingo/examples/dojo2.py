"""Classic Garoa Hardware Dojo Exercise

Light up segments on perimeter of display in sequence,
with delay set by potentiometer.

This script assumes:

- ``board.pins[13]`` is a ``DigitalPin``
- there is an LED attached to it

"""

import time
import pingo

POT_LOCATION = 'A0'
PIN_LOCATIONS = range(6, 14)

board = pingo.detect.MyBoard()
pot = pingo.pins[POT_LOCATION]
leds = (pingo.pins[loc] for loc in POT_LOCATIONS if loc != 9)

for led in leds:
    led.mode = pingo.OUT

while True:
    for led in leds:
        led.high()
        sleep(pot.ratio())
        led.low()
