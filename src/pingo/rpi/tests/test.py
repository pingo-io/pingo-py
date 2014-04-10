import os
import sys
import unittest

sys.path.append("../../..")

import pingo


class RaspberryiBasics(unittest.TestCase):

    def test_list_pins(self):
        board = pingo.rpi.RaspberryPi()
        vdd_pin = board.pins[1]
        self.assertIsInstance(vdd_pin, pingo.board.VddPin)

        pin = board.pins[7]
        self.assertIsInstance(pin, pingo.board.DigitalPin)

        self.assertEqual(len(board.pins), 26)

    def test_enable_pin(self):
        board = pingo.rpi.RaspberryPi()
        pin = board.pins[7]
        self.assertiFalse(os.path.isfile("/sys/class/gpio/gpio4"))

        board.enable_pin(pin)
        self.assertTrue(os.path.isfile("/sys/class/gpio/gpio4"))

        board.desable_pin(pin)
        self.assertFalse(os.path.isfile("/sys/class/gpio/gpio4"))


    def test_led(self):
        board = pingo.rpi.RaspberryPi()
        pin = board.pins[7]
        board.enable_pin(pin)
        pin.set_mode(OUTPUT)
        pin.high()
        board.desable_pin(pin)


if __name__ == '__main__':
    unittest.main()

