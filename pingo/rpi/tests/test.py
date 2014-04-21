import os
import sys
import unittest
import time

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
        pin.mode = pingo.OUT
        pin.high()

class RaspberryDigitalInput(RaspberryTest):

    def test_button(self):
        pin = self.board.pins[8]
        pin.mode = pingo.IN

        t0 = time.time()
        delay = 5
        output = 0
        while output == 0:
            output = pin.state
            if time.time() - t0 > delay:
                break

        msg = 'The button must be pressed in %ss for this test to pass' % delay
        self.assertEqual(output, 1, msg)


class RaspberryExceptions(RaspberryTest):

    def test_disabled_pin(self):
        pin = self.board.pins[7]
        with self.assertRaises(pingo.DisabledPin) as cm:
            pin.high()

    def test_wrong_pin_mode_in(self):
        pin = self.board.pins[7]
        pin.mode = pingo.IN
        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.high()

    @unittest.skip("Discuss about this case")
    def test_wrong_pin_mode_out(self):
        pin = self.board.pins[7]
        pin.mode = pingo.OUT
        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.state



if __name__ == '__main__':
    unittest.main()

