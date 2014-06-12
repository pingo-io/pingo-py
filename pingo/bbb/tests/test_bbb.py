import os
import sys
import time
import unittest

import pingo
from pingo.test import level0
from pingo.detect import check_board

running_on_beaglebone = check_board(pingo.bbb.BeagleBoneBlack)


class BeagleBoneBlackTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.bbb.BeagleBoneBlack()
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 0
        self.digital_input_pin_number = 0
        self.total_pins = 0

    def tearDown(self):
        self.board.cleanup()


@unittest.skipIf(not running_on_beaglebone,
    "BeagleBoneBlack not detected")
class BeagleBoneBlackBasics(BeagleBoneBlackTest, level0.BoardBasics):
    pass


@unittest.skipIf(not running_on_beaglebone,
    "BeagleBoneBlack not detected")
class BeagleBoneBlackExceptions(BeagleBoneBlackTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()