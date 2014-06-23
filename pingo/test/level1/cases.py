import os
import sys
import time
import unittest

import pingo


'''
In order to use this set of cases, it is necessary to set
the following attributes on your TestCase setUp:
    self.analog_input_pin_number = 0
    self.expected_analog_input = 1004
    self.expected_analog_ratio = 0.98
'''

class AnalogReadBasics(object):
    '''
        Wire a 10K Ohm resistence from the AnalogPin to the GND.
        Then wire a 200 Ohm from the AnalogPin to the VND.
        This schema will provide a read of ~98%
    '''

    def test_200ohmRead(self):
        pin = self.board.pins[self.analog_input_pin_number]
        pin.mode = pingo.IN
        _input = pin.value
        #print "Value Read: ", _input

        assert self.expected_analog_input-3 <= _input <= self.expected_analog_input+3

    def test_pin_ratio(self):
        pin = self.board.pins[self.analog_input_pin_number]
        pin.mode = pingo.IN
        bits_resolution = (2 ** pin.bits) - 1
        _input = pin.ratio(0, bits_resolution, 0.0, 1.0)
        #print "Value Read: ", _input

        # Two decimal places check
        assert abs(_input - self.expected_analog_ratio) < 10e-1


class AnalogExceptions(object):

    def test_wrong_output_mode(self):
        pin = self.board.pins[self.analog_input_pin_number]
        with self.assertRaises(pingo.ModeNotSuported):
            pin.mode = pingo.OUT

