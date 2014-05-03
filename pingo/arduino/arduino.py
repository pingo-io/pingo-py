
"""
Arduino
"""

import platform

from pingo.board import Board, AnalogInputCapable, DigitalPin, AnalogPin
from pingo.board import IN, OUT, HIGH, LOW
from pingo.detect import detect

DIGITAL_PIN_MODES = {IN: 0, OUT: 1}
DIGITAL_PIN_STATES = {HIGH: 1, LOW: 0}
LEN_DIGITAL_PINS = 14  # FIXME: this is not true for all Arduino boards
LEN_ANALOG_PINS = 6  # FIXME: this is not true for all Arduino boards
# FIXME: Firmata provides board info, but pyFirmata does not support this
# feature yet


def get_arduino():
    serial_port = detect._find_arduino_dev(platform.system())
    if not serial_port:
        raise LookupError('Serial port not found')
    return ArduinoFirmata(serial_port)


class ArduinoFirmata(Board, AnalogInputCapable):

    def __init__(self, port=None):
        try:
            import pyfirmata
        except ImportError:
            msg = 'pingo.arduino.Arduino requires pyfirmata installed'
            raise SystemExit(msg)

        super(ArduinoFirmata, self).__init__()
        self.port = port
        try:
            self.firmata = pyfirmata.Arduino(self.port)
        except OSError:
            raise OSError('Could find %r' % self.port)

        self.serial_iterator = pyfirmata.util.Iterator(self.firmata)
        self.serial_iterator.daemon = True

        self.add_pins([DigitalPin(self, location)
                            for location in range(LEN_DIGITAL_PINS)] +
                      [AnalogPin(self, 'A%s' % location, bits=10)
                            for location in range(LEN_ANALOG_PINS)])

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{cls_name} {self.port!r}>'.format(**locals())

    def _set_pin_mode(self, pin, state):
        pass

    def _set_pin_state(self, pin, state):
        assert state in DIGITAL_PIN_STATES, '%r not in %r' % (
            state, DIGITAL_PIN_STATES)
        self.firmata.digital[pin.location].write(DIGITAL_PIN_STATES[state])

    def _get_pin_value(self, pin):
        if not self.serial_iterator.is_alive():
            self.serial_iterator.start()
        analog_id = int(pin.location[1:])
        firmata_pin = self.firmata.analog[analog_id]
        if not firmata_pin.reporting:
            firmata_pin.enable_reporting()
        value = firmata_pin.read()
        while value is None:
            value = firmata_pin.read()
        return value



