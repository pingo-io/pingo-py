from time import sleep

import pingo

gg = pingo.galileo.Galileo2()

pins = gg.digital_pins[8:14] + gg.digital_pins[7]

d7 = pingo.parts.led.SevenSegment(*pins)

for i in range(16):
    d7.digit = i
    sleep(.5)
