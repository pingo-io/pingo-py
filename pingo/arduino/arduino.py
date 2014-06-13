
"""
Arduino
"""

import time
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

MAX_BAUD_RATE = 57600  # for Firmata serial communication

def get_arduino():
    serial_port = detect._find_arduino_dev(platform.system())
    if not serial_port:
        raise LookupError('Serial port not found')
    return ArduinoFirmata(serial_port)


class ArduinoFirmata(Board, AnalogInputCapable):

    def __init__(self, port=None, baud_rate=MAX_BAUD_RATE):
        try:
            import pyfirmata
        except ImportError:
            msg = 'pingo.arduino.Arduino requires pyfirmata installed'
            raise SystemExit(msg)

        super(ArduinoFirmata, self).__init__()
        self.port = port
        self.baud_rate = baud_rate
        try:
            self.firmata = pyfirmata.Arduino(self.port, baudrate=self.baud_rate)
        except OSError:
            raise OSError('Could find %r' % self.port)

        self.serial_iterator = pyfirmata.util.Iterator(self.firmata)
        self.serial_iterator.daemon = True

        self._add_pins([DigitalPin(self, location)
                            for location in range(LEN_DIGITAL_PINS)] +
                      [AnalogPin(self, 'A%s' % location, resolution=10)
                            for location in range(LEN_ANALOG_PINS)])

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{cls_name} {self.port!r}>'.format(**locals())

    def _set_pin_mode(self, pin, mode):
        assert mode in [IN, OUT]
        firmata_pin = self.firmata.digital[pin.location]
        if mode == OUT:
            #firmata_pin.mode = pyfirmata.OUTPUT
            firmata_pin.mode = 1
        elif mode == IN:
            #firmata_pin.mode = pyfirmata.INPUT
            firmata_pin.mode = 0

    def _get_pin_state(self, pin):
        if not self.serial_iterator.is_alive():
            self.serial_iterator.start()

        digital_id = int(pin.location)
        firmata_pin = self.firmata.digital[digital_id]

        if not firmata_pin.reporting:
            firmata_pin.enable_reporting()

        # TODO: .read() returns the pyfirmata.Pin.value attribute.
        # so if this variable is set to None, it will always return None
        state = firmata_pin.read()

        if state == 1:
            return HIGH
        elif state == 0:
            return LOW

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
            time.sleep(0.01)
        return int(value * ((2 ** pin.bits) - 1))

