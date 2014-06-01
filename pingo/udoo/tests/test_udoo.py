import os
import sys
import time
import unittest

import pingo
from pingo.test import level0
from pingo.detect import check_board

running_on_udoo = check_board(pingo.udoo.Udoo)


class UdooTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.udoo.Udoo()
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 0
        self.digital_input_pin_number = 0
        self.total_pins = 0

    def tearDown(self):
        self.board.cleanup()

@unittest.skipIf(not running_on_udoo, 'Udoo not detected')
class UdooBasics(UdooTest, level0.BoardBasics):
    pass


@unittest.skipIf(not running_on_udoo, 'Udoo not detected')
class UdooExceptions(UdooTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()