import sys
from time import sleep

import pingo

ard = pingo.arduino.get_arduino()

print('Found: %r' % ard)

pin = ard.pins['A0']

while True:
    sleep(.02)
    print '%4d' % pin.value, int(70 * pin.ratio()) * '*'
