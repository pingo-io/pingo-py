import os
import sys
import unittest
import time

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


class GhostBoardBasics(GhostBoardTest, level0.BoardBasics):
    pass

class GhostBoardExceptions(GhostBoardTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
