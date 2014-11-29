from time import sleep

import pingo

gg = pingo.detect.MyBoard()

pins = gg.select_pins(range(8, 14) + [7])

d7 = pingo.parts.led.SevenSegments(*pins)

for char in 'GAr0A':
    try:
        d7.digit = int(char, 16)
    except ValueError:
        d7.digit = char
    sleep(.5)
