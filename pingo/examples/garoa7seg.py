from time import sleep

import pingo

board = pingo.detect.MyBoard()

pins = [gg.pins[i] for i in range(8, 14) + [7]]

d7 = pingo.parts.led.SevenSegments(*pins)

for char in range('GAr0A'):
    try:
        d7.digit = int(char, 16)
    except ValueError:
        d7.digit = char
    sleep(.5)
