import os
import sys
import time
import unittest

import pingo


'''
In order to use this set of cases, it is necessery to set
the following atributes on your TestCase setUp:
    self.vdd_pin_number = 2
    self.digital_output_pin_number = 13
    self.digital_input_pin_number = 8
    self.total_pins = 26
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
        pin.on()

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
            pin.on()

    def test_wrong_pin_mode_in(self):
        pin = self.board.pins[self.digital_input_pin_number]
        pin.mode = pingo.IN

        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.on()

        with self.assertRaises(pingo.WrongPinMode) as cm:
            pin.state = pingo.HIGH


#    def test_wrong_pin_mode_out(self):
#        pin = self.board.pins[digital_output_pin_number]
#        pin.mode = pingo.OUT
#        with self.assertRaises(pingo.WrongPinMode) as cm:
#            pin.state

