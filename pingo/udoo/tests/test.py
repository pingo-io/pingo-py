import os
import sys
import unittest

sys.path.append("../../..")

import pingo

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.udoo.Udoo()

    def tearDown(self):
        self.board.cleanup()


class BoardBasics(BoardTest):

    def test_list_pins(self):
        pin = self.board.pins[13]
        self.assertIsInstance(pin, pingo.DigitalPin)

    def test_led(self):
        pin = self.board.pins[13]
        pin.set_mode(pingo.OUT)
        pin.high()


class BoardExceptions(BoardTest):

    def test_wrong_pin_mode(self):
        pin = self.board.pins[7]
        pin.set_mode(pingo.IN)
        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.high()


if __name__ == '__main__':
    unittest.main()

