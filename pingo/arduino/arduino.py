
"""
Arduino
"""

from pingo.board import Board, DigitalPin, IN, OUT, HIGH, LOW

DIGITAL_PIN_MODES = {IN: 0, OUT: 1}
DIGITAL_PIN_STATES = {HIGH: 0, LOW: 1}
LEN_DIGITAL_PINS = 14  # FIXME: this is not true for all Arduino boards
# FIXME: Firmata provides board info, but pyFirmata does not support this
# feature yet


class ArduinoFirmata(Board):

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

        self.add_pins(DigitalPin(self, location)
                      for location in range(LEN_DIGITAL_PINS))

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{cls_name} {self.port!r}>'.format(**locals())

    def _set_pin_mode(self, pin, state):
        pass

    def _set_pin_state(self, pin, state):
        assert state in DIGITAL_PIN_STATES, '%r not in %r' % (
            state, DIGITAL_PIN_STATES)
        self.firmata.digital[pin.location].write(DIGITAL_PIN_STATES[state])
