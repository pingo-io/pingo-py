import os
import sys
import unittest

sys.path.append("../../..")

import pingo

class RaspberryTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.rpi.RaspberryPi()

    def tearDown(self):
        self.board.cleanup()


class RaspberryBasics(RaspberryTest):

    def test_list_pins(self):
        vdd_pin = self.board.pins[1]
        self.assertIsInstance(vdd_pin, pingo.VddPin)

        pin = self.board.pins[7]
        self.assertIsInstance(pin, pingo.DigitalPin)

        self.assertEqual(len(self.board.pins), 26)

    def test_led(self):
        pin = self.board.pins[7]
        pin.set_mode(pingo.OUTPUT)
        pin.high()


class RaspberryExceptions(RaspberryTest):

    def test_disabled_pin(self):
        pin = self.board.pins[7]
        with self.assertRaises(pingo.DisabledPin) as cm:
            pin.high()

    def test_wrong_pin_mode(self):
        pin = self.board.pins[7]
        pin.set_mode(pingo.INPUT)
        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.high()


if __name__ == '__main__':
    unittest.main()

