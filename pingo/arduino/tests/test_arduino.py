import sys
import platform
import unittest

import pingo
from pingo.test import level0
from pingo.test import level1
from pingo.detect import has_module, check_board

running_on_arduino = check_board(pingo.arduino.ArduinoFirmata)

class ArduinoFirmataTest(unittest.TestCase):

    def setUp(self):
        device = pingo.detect.detect._find_arduino_dev(platform.system())
        self.board = pingo.arduino.ArduinoFirmata(device)

        # Level0 Parameters
        #self.vdd_pin_number = 0
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 2
        self.total_pins = 14

        # Level1 Parameters
        self.analog_input_pin_number = 'A4'
        self.expected_analog_input = 1004
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        self.board.cleanup()


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('PyMata'),
    'pingo.arduino.Arduino requires PyMata installed')
class ArduinoBasics(ArduinoFirmataTest, level0.BoardBasics):
    @unittest.skip('ArduinoFirmata does not recognize VddPins')
    def test_list_pins(self):
        pass


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('PyMata'),
    'pingo.arduino.Arduino requires PyMata installed')
class ArduinoDigitalExceptions(ArduinoFirmataTest, level0.BoardExceptions):
    pass


@unittest.skipIf(not running_on_arduino, "Arduino not detected")
@unittest.skipIf(not has_module('PyMata'),
    "pingo.arduino.Arduino requires PyMata installed")
class ArduinoAnalogRead(ArduinoFirmataTest, level1.AnalogReadBasics):
    pass


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('PyMata'),
    'pingo.arduino.Arduino requires PyMata installed')
class ArduinoAnalogExceptions(ArduinoFirmataTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
