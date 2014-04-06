
"""
UDOO board

Reference:
http://www.udoo.org/ProjectsAndTutorials/linux-gpio-manipulation/
"""

import os

from pingo.board import Board, DigitalPin, INPUT, OUTPUT

# there are no gaps in the Arduino digital pin numbering
# of the Arduino Due embedded in the Udoo

# pin_list[physical_arduino_pin] -> logical_gpio_pin
pin_list = [
    116, 112, 20, 16, 17, 18, 41, 42, 21, 19, 1, 9, 3, 40, # <-- 13
    150, 162, 160, 161, 158, 159, 92, 85, 123, 124, 125, 126, 127,
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 54, 205,
    32, 35, 34, 33, 101, 144, 145, 89, 105, 104, 57, 56, 55, 88
]

# /sys/class/gpio/gpio40/ --> Arduino pin #13
DIGITAL_PINS_PATH = '/sys/class/gpio'
DIGITAL_PIN_MASK = 'gpio%d'
DIGITAL_PIN_STATE_FILENAME = 'value'
DIGITAL_PIN_MODE_FILENAME = 'direction'
DIGITAL_PIN_MODES = {INPUT: 'in', OUTPUT: 'out'}

class Udoo(Board):

    def __init__(self):

        Board.__init__(self)
        self.add_pins(self._list_pins())
        self.pin_path_mask = '/sys/class/gpio/gpio%d/'

    def _list_pins(self):
        pins = []
        for location, gpio_id in enumerate(pin_list):
            path = self._base_pin_path(gpio_id)
            if os.path.exists(path):
                pins.append(DigitalPin(self, location, gpio_id))
        return pins

    def _base_pin_path(self, gpio_id):
        return os.path.join(DIGITAL_PINS_PATH, DIGITAL_PIN_MASK % gpio_id)

    def _pin_mode_filename(self, gpio_id):
        path = self._base_pin_path(gpio_id)
        return os.path.join(path, DIGITAL_PIN_MODE_FILENAME)

    def _pin_state_filename(self, gpio_id):
        return os.path.join(self._base_pin_path(gpio_id), DIGITAL_PIN_STATE_FILENAME)

    def set_pin_mode(self, pin, mode):
        assert mode in DIGITAL_PIN_MODES, '%r not in %r' % (mode, DIGITAL_PIN_MODES)
        with open(self._pin_mode_filename(pin.gpio_id), "wb") as fp:
            fp.write(DIGITAL_PIN_MODES[mode])

    def set_pin_state(self, pin, state):
        with open(self._pin_state_filename(pin.gpio_id), "wb") as fp:
            fp.write(str(state))


