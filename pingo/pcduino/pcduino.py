
"""
pcDuino v1 board
"""

import os

from pingo.board import Board, DigitalPin, INPUT, OUTPUT

# /sys/class/gpio/gpio40/ --> Arduino pin #13
DIGITAL_PINS_PATH = '/sys/devices/virtual/misc/gpio/'
DIGITAL_PIN_MODES = {INPUT: '0', OUTPUT: '1'}

class PcDuino(Board):

    def __init__(self):
        self.add_pins(DigitalPin(self, location)
                for location in range(14))

    def set_pin_mode(self, pin, mode):
        assert mode in DIGITAL_PIN_MODES, '%r not in %r' % (mode, DIGITAL_PIN_MODES)
        with open(DIGITAL_PINS_PATH+'mode/gpio%s' % pin.location, 'w') as fp:
            fp.write(DIGITAL_PIN_MODES[mode])

    def set_pin_state(self, pin, state):
        with open(DIGITAL_PINS_PATH+'pin/gpio%s' % pin.location, 'w') as fp:
            fp.write(str(state))


