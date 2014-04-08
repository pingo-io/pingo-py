import sys
import unittest

sys.path.append("../../..")

import pingo

class Raspberry(unittest.TestCase):

    def test_list_pins(self):
        board = pingo.rpi.RaspberryPi()
        vdd_pin = board.pins[1]
        self.assertIsInstance(vdd_pin, pingo.board.VddPin)
        pin = board.pins[7]
        self.assertIsInstance(pin, pingo.board.DigitalPin)
        self.assertEqual(len(board.pins) ,26)

    def test_enable_pin(self):
        board = pingo.rpi.RaspberryPi()
        pin = board.pins[7]
        board.enable_pin(pin)


    def test_led(self):
        board = pingo.rpi.RaspberryPi()
        pin = board.pins[7]
        board.enable_pin(pin)

if __name__ == '__main__':
    unittest.main()

