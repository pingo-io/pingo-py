from time import sleep

import pingo

gg = pingo.galileo.Galileo2()

pins = [gg.pins[i] for i in range(8, 14) + [7]]

d7 = pingo.parts.led.SevenSegments(*pins)

for i in range(16):
    d7.digit = i
    sleep(.5)
