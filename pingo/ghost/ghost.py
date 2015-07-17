import pingo


class GhostBoard(
    pingo.Board,
    pingo.AnalogInputCapable,
    pingo.PwmOutputCapable
):

    def __init__(self, filepath=None):
        super(GhostBoard, self).__init__()

        # Arduino ATmega168/328 pin mapping
        pins = set([
            pingo.DigitalPin(self, 0),
            pingo.DigitalPin(self, 1),
            pingo.DigitalPin(self, 2),
            pingo.PwmPin(self, 3),
            pingo.DigitalPin(self, 4),

            pingo.VccPin(self, 'VCC', 5.0),
            pingo.GroundPin(self, 'GND'),
            pingo.PwmPin(self, 5),
            pingo.PwmPin(self, 6),
            pingo.DigitalPin(self, 7),

            pingo.DigitalPin(self, 8),
            pingo.AnalogPin(self, 'A5', 10),
            pingo.AnalogPin(self, 'A4', 10),
            pingo.AnalogPin(self, 'A3', 10),
            pingo.AnalogPin(self, 'A2', 10),

            pingo.AnalogPin(self, 'A1', 10),
            pingo.AnalogPin(self, 'A0', 10),
            pingo.GroundPin(self, 'GND'),
            pingo.VccPin(self, 'AREF', 5.0),
            pingo.VccPin(self, 'AVCC', 5.0),

            pingo.DigitalPin(self, 12),
            pingo.DigitalPin(self, 13),
            pingo.PwmPin(self, 11),
            pingo.PwmPin(self, 10),
            pingo.PwmPin(self, 9),
        ])

        self._add_pins(pins)

        self._pin_states = pingo.util.StrKeyDict()
        # All pins start on LOW
        # FIXME: use "LOW" instead of 0
        for location, pin in self.pins.iteritems():
            self._pin_states[location] = 0 if hasattr(pin, 'state') else None

        # Pin 8 starts on HIGH
        self._pin_states[8] = 1

    def cleanup(self):
        print('GhostBoard: cleaning up.')

    def _set_digital_mode(self, pin, mode):
        print('GhostBoard: %r mode -> %s' % (pin, mode))

    def _set_analog_mode(self, pin, mode):
        self._set_digital_mode(pin, mode)

    def _set_pwm_mode(self, pin, mode):
        self._set_digital_mode(pin, mode)

    def _set_pin_state(self, pin, state):
        print('GhostBoard: %r state -> %s' % (pin, state))
        _state = 1 if state == pingo.HIGH else 0
        self._pin_states[pin.location] = _state

    def _get_pin_state(self, pin):
        state = self._pin_states[pin.location]
        return pingo.HIGH if state else pingo.LOW

    def _get_pin_value(self, pin):
        return self._pin_states[pin.location]

    def _get_pwm_duty_cycle(self, pin):
        return self._pin_states[pin.location]

    def _set_pwm_duty_cycle(self, pin, value):
        self._pin_states[pin.location] = value

    def _set_pwm_frequency(self, pin, value):
        pass
