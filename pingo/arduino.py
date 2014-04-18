
"""
Arduino
"""

import os

from pingo.board import Board, DigitalPin, IN, OUT

DIGITAL_PIN_MODES = {IN: 0, OUT: 1}

class Arduino(Board):
    LEN_DIGITAL_PINS = 14

    def __init__(self, port=None):
        try:
            from pyfirmata import Arduino as ArduinoFirmata
        except ImportError:
            raise SystemExit('pingo.arduino.Arduino requires pyfirmata installed')

        super(Arduino, self).__init__()

        self.ard_firmata = ArduinoFirmata(port)
        self.add_pins(DigitalPin(self, location)
                        for location in LEN_DIGITAL_PINS)

    def _set_pin_state(self, pin, state):
        board.digital[13].write(1)
