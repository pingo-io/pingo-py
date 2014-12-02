import unittest

import pingo

from pingo.test import level0
from pingo.test import level1
from pingo.test import level2


class GhostBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.ghost.GhostBoard()

        # Level1 Parameters
        self.vdd_pin_number = 'VCC'
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 8
        self.total_pins = 24

        # Level1 Parameters
        self.analog_input_pin_number = 'A4'
        self.expected_analog_input = 1004
        self.expected_analog_ratio = 0.98
        self.board._pin_states['A4'] = 1004  # Workaround

        # Level2 Parameters
        self.pwm_pin_number = 3

    def tearDown(self):
        self.board.cleanup()


class GhostBoardBasics(GhostBoardTest, level0.BoardBasics):
    pass


class GhostBoardExceptions(GhostBoardTest, level0.BoardExceptions):
    pass


class GhostAnalogRead(GhostBoardTest, level1.AnalogReadBasics):
    pass


class GhostAnalogExceptions(GhostBoardTest, level1.AnalogExceptions):
    pass


class GhostPwm(GhostBoardTest, level2.PwmBasics):
    pass


class GhostPwmExceptions(GhostBoardTest, level2.PwmExceptions):
    pass

if __name__ == '__main__':
    unittest.main()
