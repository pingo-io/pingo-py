import os
import sys
import unittest
import time

import pingo
from pingo.test import level0
from pingo.test import level1


class PcDuinoTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.pcduino.PcDuino()
        # Level0 Parameters
        self.digital_output_pin_number = 3
        self.digital_input_pin_number = 11
        self.total_pins = 20

        # Level1 Parameters
        self.analog_input_pin_number = 'A2'
        self.expected_analog_input = 4014
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        self.board.cleanup()


class PcDuinoBasics(PcDuinoTest, level0.BoardBasics):
    def test_list_pins(self):
        pin = self.board.pins[self.digital_output_pin_number]
        self.assertIsInstance(pin, pingo.DigitalPin)

        data_pins = len(pingo.pcduino.PcDuino().pins)
        self.assertEqual(data_pins, self.total_pins)

class PcDuinoExceptions(PcDuinoTest, level0.BoardExceptions):
    pass


class PcDuinoAnalogRead(PcDuinoTest, level1.AnalogReadBasics):
    pass


class PcDuinoAnalogExceptions(PcDuinoTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
