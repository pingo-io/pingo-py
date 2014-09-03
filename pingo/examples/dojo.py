"""Classic Garoa Hardware Dojo Exercise

Light up segments on perimeter of display in sequence,
with delay set by potentiometer.

This script assumes:

- 7-segment display connected to pins 6-13
- segment G is pin 13, decimal point is pin 9
- potentiometer connected to analog pin 'A0'

"""

import time
import pingo

board = pingo.detect.MyBoard()
print('board: %s' % board)
pot = board.pins['A0']
pot.mode = pingo.ANALOG
leds = board.digital_pins[6:14]

for led in leds:
    led.mode = pingo.OUT
    led.low()

while True:
    for led in leds:
        if led.location == 9:
            continue
        led.high()
        time.sleep(pot.ratio())
        print pot.ratio()
        led.low()
