
"""
Firmata protocol client for Pingo
Works on Arduino with the StandardFirmata sketch uploaded
"""

import time
import platform

import pingo
from pingo.board import Board, DigitalPin, AnalogPin, PwmPin
from pingo.board import AnalogInputCapable, PwmOutputCapable
from pingo.detect import detect
from util_firmata import pin_list_to_board_dict

PyMata = None

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

VERBOSE = False


def get_arduino():
    serial_port = detect._find_arduino_dev(platform.system())
    if not serial_port:
        raise LookupError('Serial port not found')
    return ArduinoFirmata(serial_port)


class ArduinoFirmata(Board, AnalogInputCapable, PwmOutputCapable):

    def __init__(self, port=None):
        try:
            from PyMata.pymata import PyMata as PyMata  # noqa
        except ImportError:
            msg = 'pingo.arduino.Arduino requires PyMata installed'
            raise ImportError(msg)

        super(ArduinoFirmata, self).__init__()
        self.port = port
        self.firmata_client = PyMata(self.port, verbose=VERBOSE)

        self.firmata_client.capability_query()
        time.sleep(10)  # TODO: Find a small and safe value
        capability_query_results = self.firmata_client.get_capability_query_results()
        capability_dict = pin_list_to_board_dict(capability_query_results)

        self._add_pins(
            [DigitalPin(self, location)
                for location in capability_dict['digital']] +
            [PwmPin(self, location)
                for location in capability_dict['pwm']] +
            [AnalogPin(self, 'A%s' % location, resolution=10)
                for location in capability_dict['analog']]
        )

    def cleanup(self):
        # self.firmata_client.close() has sys.exit(0)
        if hasattr(self, 'PyMata'):
            try:
                self.firmata_client.transport.close()
            except AttributeError:
                pass

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{cls_name} {self.port!r}>'.format(**locals())

    def _set_digital_mode(self, pin, mode):
        self.firmata_client.set_pin_mode(
            pin.location,
            PIN_MODES[mode],
            self.firmata_client.DIGITAL
        )

    def _set_analog_mode(self, pin, mode):
        pin_id = int(pin.location[1:])
        self.firmata_client.set_pin_mode(
            pin_id,
            self.firmata_client.INPUT,
            self.firmata_client.ANALOG
        )

    def _set_pwm_mode(self, pin, mode):
        pin_id = int(pin.location)
        self.firmata_client.set_pin_mode(
            pin_id,
            self.firmata_client.PWM,
            self.firmata_client.DIGITAL
        )

    def _get_pin_state(self, pin):
        _state = self.firmata_client.digital_read(pin.location)
        if _state == self.firmata_client.HIGH:
            return pingo.HIGH
        return pingo.LOW

    def _set_pin_state(self, pin, state):
        self.firmata_client.digital_write(
            pin.location,
            PIN_STATES[state]
        )

    def _get_pin_value(self, pin):
        pin_id = int(pin.location[1:])
        return self.firmata_client.analog_read(pin_id)

    def _set_pwm_duty_cycle(self, pin, value):
        pin_id = int(pin.location)
        firmata_value = int(value * 255)
        return self.firmata_client.analog_write(pin_id, firmata_value)

    def _set_pwm_frequency(self, pin, value):
        raise NotImplementedError
