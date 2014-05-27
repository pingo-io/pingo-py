import os
import sys
import time
import unittest

import pytest
from pip import get_installed_distributions

import pingo
from pingo.test import level0
from pingo.test import not_has_module


@pytest.mark.skipif(not_has_module('RPi'),
                    reason="pingo.rpi requires RPi.GPIO installed")
class RaspberryTest(unittest.TestCase):

    def setup(self):
        self.board = pingo.rpi.RaspberryPi()
        self.vdd_pin_number = 2
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 7
        self.total_pins = 26

    def tearuown(self):
        self.board.cleanup()


class RaspberryBasics(RaspberryTest, level0.BoardBasics):
    pass


class RaspberryExceptions(RaspberryTest, level0.BoardExceptions):
    pass
