import os
import sys
import time
import unittest

import pingo
from pingo.test import level0
from pingo.test import level1


class GhostBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.ghost.GhostBoard()

        # Level1 Parameters
        self.vdd_pin_number = 2
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 8
        self.total_pins = 16

        # Level1 Parameters
        self.analog_input_pin_number = 'A4'
        self.expected_analog_input = 1004
        self.expected_analog_ratio = 0.98


    def tearDown(self):
        self.board.cleanup()


class GhostBoardBasics(GhostBoardTest, level0.BoardBasics):
    pass


class GhostBoardExceptions(GhostBoardTest, level0.BoardExceptions):
    pass


#class GhostAnalogRead(GhostBoardTest, level1.AnalogReadBasics):
#    pass


#class GhostAnalogExceptions(GhostBoardTest, level1.AnalogExceptions):
#    pass


if __name__ == '__main__':
    unittest.main()
