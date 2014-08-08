
"""
Arduino
"""

import time
import platform

import pingo
from pingo.board import Board, AnalogInputCapable, DigitalPin, AnalogPin
from pingo.detect import detect

PIN_STATES = {
    False: 0,
    True: 1,
    0: 0,
    1: 1,
    pingo.LOW: 0,
    pingo.HIGH: 1,
}

# TODO: PyMata suports Input, Output, PWM, Servo, Encoder and Tone
PIN_MODES = {
    pingo.IN: 0,
    pingo.OUT: 1,
}


def get_arduino():
    serial_port = detect._find_arduino_dev(platform.system())
    if not serial_port:
        raise LookupError('Serial port not found')
    return ArduinoFirmata(serial_port)


class ArduinoFirmata(Board, AnalogInputCapable):

    def __init__(self, port=None):
        try:
            from PyMata.pymata import PyMata
        except ImportError:
            msg = 'pingo.arduino.Arduino requires PyMata installed'
            raise ImportError(msg)

        super(ArduinoFirmata, self).__init__()
        self.port = port
        self.PyMata = PyMata(self.port)

        detected_digital_pins = len(self.PyMata._command_handler.digital_response_table)
        detected_analog_pins =  len(self.PyMata._command_handler.analog_response_table)

        self._add_pins(
            [DigitalPin(self, location)
                for location in range(detected_digital_pins)] +
            [AnalogPin(self, 'A%s' % location, resolution=10)
                for location in range(detected_analog_pins)]
        )

    def cleanup(self):
        #self.PyMata.close() has sys.exit(0)
        if hasattr(self, 'PyMata'):
            try:
                self.PyMata.transport.close()
            except AttributeError:
                pass

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{cls_name} {self.port!r}>'.format(**locals())

    def _set_pin_mode(self, pin, mode):
        self.PyMata.set_pin_mode(
            pin.location,
            PIN_MODES[mode],
            self.PyMata.DIGITAL
        )

    def _get_pin_state(self, pin):
        _state = self.PyMata.digital_read(pin.location)
        if _state == self.PyMata.HIGH:
            return pingo.HIGH
        return pingo.LOW

    def _set_pin_state(self, pin, state):
        self.PyMata.digital_write(
                pin.location,
                PIN_STATES[state]
        )

    def _set_analog_mode(self, pin, mode):
        pin_id = int(pin.location[1:])
        self.PyMata.set_pin_mode(
            pin_id,
            self.PyMata.INPUT,
            self.PyMata.ANALOG
        )

    def _get_pin_value(self, pin):
        pin_id = int(pin.location[1:])
        return self.PyMata.analog_read(pin_id)

