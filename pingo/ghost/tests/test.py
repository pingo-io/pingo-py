import os
import sys
import unittest
import time

#sys.path.append('../../..')

import pingo
from pingo.test import level0

class GhostBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.ghost.GhostBoard()
        self.vdd_pin_number = 2
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 8
        self.total_pins = 16

    def tearDown(self):
        self.board.cleanup()


class GhostBoardBasics(GhostBoardTest):

    self.test_list_pins = level0.test_list_pins
    self.test_led = level0.test_led
    self.button = level0.test_button

if __name__ == '__main__':
    unittest.main()

