import unittest
import platform

import pingo
from pingo.test import level0

class ArduinoFirmataTest(unittest.TestCase):

    def setUp(self):
        device = pingo.detect.detect._find_arduino_dev(platform.system())
        self.board = pingo.arduino.ArduinoFirmata(device)
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 12
        self.total_pins = 14

    def tearDown(self):
        self.board.cleanup()


class ArduinoBasics(ArduinoFirmataTest, level0.BoardBasics):

    @unittest.skip('TODO: decide on the API to list all pins on an Arduino')
    def test_list_pins(self):
        pass

    @unittest.skip('This needs a jumper from Vdd to digital_input_pin_number')
    def test_jumpwire(self):
        pass

class ArduinoExceptions(ArduinoFirmataTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
