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
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 12
        self.total_pins = 14

        # Level1 Parameters
        self.analog_input_pin_number = 'A4'
        self.expected_analog_input = 1004
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        self.board.cleanup()


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('pyfirmata'),
    'pingo.arduino.Arduino requires pyfirmata installed')
class ArduinoBasics(ArduinoFirmataTest, level0.BoardBasics):
    @unittest.skip('TODO: decide on the API to list all pins on an Arduino')
    def test_list_pins(self):
        pass

    @unittest.skip('Unsupported by pyFirmata')
    def test_jumpwire(self):
        pass


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('pyfirmata'),
    'pingo.arduino.Arduino requires pyfirmata installed')
class ArduinoDigitalExceptions(ArduinoFirmataTest, level0.BoardExceptions):
    pass


@unittest.skipIf(not running_on_arduino, "Arduino not detected")
@unittest.skipIf(not has_module('pyfirmata'),
    "pingo.arduino.Arduino requires pyfirmata installed")
class ArduinoAnalogRead(ArduinoFirmataTest, level1.AnalogReadBasics):
    pass


@unittest.skipIf(not running_on_arduino, 'Arduino not detected')
@unittest.skipIf(not has_module('pyfirmata'),
    'pingo.arduino.Arduino requires pyfirmata installed')
class ArduinoAnalogExceptions(ArduinoFirmataTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
