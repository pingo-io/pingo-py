import os
import sys
import unittest
import time

import pingo
from pingo.test import level0


class RaspberryTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.rpi.RaspberryPi()
        self.vdd_pin_number = 2
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 7
        self.total_pins = 26

    def tearDown(self):
        self.board.cleanup()


class RaspberryBasics(RaspberryTest, level0.BoardBasics):
    pass


class RaspberryExceptions(RaspberryTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()

