import unittest

import pingo
from pingo.test import level0
from pingo.test import level1
from pingo.detect import check_board

running_on_galileo = check_board(pingo.galileo.Galileo2)


class GalileoTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.galileo.Galileo2()
        # Level0 Parameters
        self.digital_output_pin_number = 6
        self.digital_input_pin_number = 3
        self.total_pins = 20

        # Level1 Parameters
        self.analog_input_pin_number = 'A3'
        self.expected_analog_input = 4096
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        pass
        # self.board.cleanup()


@unittest.skipIf(not running_on_galileo, 'Galileo not detected')
class GalileoBasics(GalileoTest, level0.BoardBasics):
    def test_list_pins(self):
        pin = self.board.pins[self.digital_output_pin_number]
        assert isinstance(pin, pingo.DigitalPin)

        data_pins = len(self.board.pins)
        assert data_pins == self.total_pins


@unittest.skipIf(not running_on_galileo, 'Galileo not detected')
class GalileoExceptions(GalileoTest, level0.BoardExceptions):
    pass


@unittest.skipIf(not running_on_galileo, 'Galileo not detected')
class GalileoAnalogRead(GalileoTest, level1.AnalogReadBasics):
    pass


@unittest.skipIf(not running_on_galileo, 'Galileo not detected')
class GalileoAnalogExceptions(GalileoTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
