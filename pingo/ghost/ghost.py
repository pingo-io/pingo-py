import os

import pingo


class GhostBoard(pingo.Board):

    def __init__(self, filepath=None):
        super(GhostBoard, self).__init__()

        pins = set([
            pingo.GroundPin(self, 1),
            pingo.VccPin(self, 2, 5.0),
            pingo.DigitalPin(self, 3),
            pingo.DigitalPin(self, 4),
            pingo.DigitalPin(self, 5),
            pingo.DigitalPin(self, 6),
            pingo.DigitalPin(self, 7),
            pingo.DigitalPin(self, 8),
            pingo.DigitalPin(self, 9),
            pingo.DigitalPin(self, 10),
            pingo.DigitalPin(self, 11),
            pingo.DigitalPin(self, 12),
            pingo.DigitalPin(self, 13),
            pingo.DigitalPin(self, 14),
            pingo.GroundPin(self, 15),
            pingo.VccPin(self, 16, 3.3),
        ])

        self._add_pins(pins)

        self.pin_states = pingo.util.StrKeyDict()
        # All pins start on LOW
        # FIXME: use "LOW" instead of 0
        for location, pin in self.pins.iteritems():
            self.pin_states[location] = 0 if hasattr(pin, 'state') else None

        # Pin 8 starts on HIGH
        self.pin_states[8] = 1

    def cleanup(self):
        print('GhostBoard: cleaning up.')

    def _set_pin_mode(self, pin, mode):
        print('GhostBoard: %r mode -> %s' % (pin, mode))

    def _set_pin_state(self, pin, state):
        print('GhostBoard: %r state -> %s' % (pin, state))
        _state = 1 if state == pingo.HIGH else 0
        self.pin_states[pin.location] = _state

    def _get_pin_state(self, pin):
        state = self.pin_states[pin.location]
        return pingo.HIGH if state else pingo.LOW

