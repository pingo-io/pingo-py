import os
import sys
import time
import unittest

import pingo
from pingo.test import level0
from pingo.test import level1
from pingo.detect import check_board

running_on_pcduino = check_board(pingo.pcduino.PcDuino)

class PcDuinoTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.pcduino.PcDuino()
        # Level0 Parameters
        self.digital_output_pin_number = 3
        self.digital_input_pin_number = 0
        self.total_pins = 20

        # Level1 Parameters
        self.analog_input_pin_number = 'A3'
        self.expected_analog_input = 4096
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        self.board.cleanup()


@unittest.skipIf(not running_on_pcduino, 'PcDuino not detected')
class PcDuinoBasics(PcDuinoTest, level0.BoardBasics):
    def test_list_pins(self):
        pin = self.board.pins[self.digital_output_pin_number]
        assert isinstance(pin, pingo.DigitalPin)

        data_pins = len(self.board.pins)
        assert data_pins == self.total_pins


@unittest.skipIf(not running_on_pcduino, 'PcDuino not detected')
class PcDuinoExceptions(PcDuinoTest, level0.BoardExceptions):
    pass


@unittest.skipIf(not running_on_pcduino, 'PcDuino not detected')
class PcDuinoAnalogRead(PcDuinoTest, level1.AnalogReadBasics):
    pass


@unittest.skipIf(not running_on_pcduino, 'PcDuino not detected')
class PcDuinoAnalogExceptions(PcDuinoTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
