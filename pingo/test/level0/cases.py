import os
import sys
import time
import unittest

import pingo


'''
In order to use this set of cases, it is necessary to set
the following attributes on your TestCase setUp:
    self.vdd_pin_number = 2
    self.digital_output_pin_number = 13
    self.digital_input_pin_number = 8
    self.total_pins = 26

AND the VDD pin must be connected to the digital_input_pin_number
'''

class BoardBasics(object):
    def test_list_pins(self):
        vdd_pin = self.board.pins[self.vdd_pin_number]
        self.assertIsInstance(vdd_pin, pingo.VddPin)

        pin = self.board.pins[self.digital_output_pin_number]
        self.assertIsInstance(pin, pingo.DigitalPin)

        self.assertEqual(len(self.board.pins), self.total_pins)

    def test_led(self):
        pin = self.board.pins[self.digital_output_pin_number]
        pin.mode = pingo.OUT
        pin.high()

    def test_filter(self):
        pins_subset = self.board.filter_pins(pingo.DigitalPin)
        self.assertTrue(
            all(isinstance(pin ,pingo.DigitalPin) for pin in pins_subset)
        )

        other_pins = set(self.board.pins.values()) - set(pins_subset)
        self.assertFalse(
            any(isinstance(pin, pingo.DigitalPin) for pin in other_pins)
        )

    @unittest.skip("Not automatic enough.")
    def test_button(self):
        pin = self.board.pins[self.digital_input_pin_number]
        pin.mode = pingo.IN
        output = pingo.LOW
        t0 = time.time()
        delay = 5

        while output == pingo.LOW:
            output = pin.state
            if time.time() - t0 > delay:
                break

        msg = 'The button must be pressed in %ss for this test to pass' % delay
        self.assertEqual(output, pingo.HIGH, msg)

    def test_jumpwire(self):
        ''' Wire this DigitalPin directly into VDD '''
        pin = self.board.pins[self.digital_input_pin_number]
        pin.mode = pingo.IN
        output = pin.state

        self.assertEqual(output, pingo.HIGH)



class BoardExceptions(object):

    def test_disabled_pin(self):
        pin = self.board.pins[self.digital_output_pin_number]
        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.high()

    def test_wrong_pin_mode_in(self):
        pin = self.board.pins[self.digital_input_pin_number]
        pin.mode = pingo.IN

        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.high()

        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.state = pingo.HIGH


#    def test_wrong_pin_mode_out(self):
#        pin = self.board.pins[digital_output_pin_number]
#        pin.mode = pingo.OUT
#        with self.assertRaises(pingo.WrongPinMode) as cm:
#            pin.state

