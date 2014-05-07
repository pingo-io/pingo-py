import os
import sys
import unittest
import time

import pingo
from pingo.test import level0

class PcDuinoTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.pcduino.PcDuino()
        self.digital_output_pin_number = 3
        self.digital_input_pin_number = 11
        self.total_pins = 20

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


if __name__ == '__main__':
    unittest.main()
