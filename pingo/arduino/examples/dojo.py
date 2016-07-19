from time import sleep

import pingo

ard = pingo.arduino.get_arduino()

display_map = {'a': 12, 'b': 13, 'c': 7, 'd': 8, 'e': 9, 'f': 11}  # 'g': 10, 'dp': 6

pins = [ard.pins[p] for p in sorted(display_map.values())]

for pin in pins:
    pin.mode = pingo.OUT

pot = ard.pins['A0']

while True:
    for pin in pins:
        pin.high()
        sleep(pot.ratio())
        pin.low()
