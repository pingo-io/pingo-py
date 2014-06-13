import os
import json

import pingo

PIN_STATES_FILEPATH = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ), 'pin_states.json')


class GhostBoard(pingo.Board):

    def __init__(self):
        super(GhostBoard, self).__init__()

        pins = set([
            pingo.GroundPin(self, 1),
            pingo.VddPin(self, 2, 5.0),
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
            pingo.VddPin(self, 16, 3.3),
        ])

        self._add_pins(pins)

        pin_states = {}
        # All pins start on LOW
        # FIXME: use "LOW" instead of 0
        for location, pin in self.pins.iteritems():
            pin_states[location] = 0 if hasattr(pin, 'state') else None

        # Pin 8 starts on HIGH
        pin_states[8] = 1

        with open(PIN_STATES_FILEPATH, 'w') as fp:
            json.dump(pin_states, fp, indent=4)

    def cleanup(self):
        print('GhostBoard: cleaning up.')

    def _set_pin_mode(self, pin, mode):
        print('GhostBoard: %r mode -> %s' % (pin, mode))

    def _set_pin_state(self, pin, state):
        print('GhostBoard: %r state -> %s' % (pin, state))
        _state = 1 if state == pingo.HIGH else 0
        with open(PIN_STATES_FILEPATH, 'r') as fp:
            pin_states = json.load(fp)
            pin_states[str(pin.location)] = _state

        with open(PIN_STATES_FILEPATH, 'w') as fp:
            json.dump(pin_states, fp, indent=4)

    def _get_pin_state(self, pin):
        with open(PIN_STATES_FILEPATH, 'r') as fp:
            pin_states = json.load(fp)
            state = pin_states[str(pin.location)]
        return  pingo.HIGH if state else pingo.LOW

