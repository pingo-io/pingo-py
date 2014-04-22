import os
import json

import pingo

PINS_STATE_FILEPATH = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ), 'pins_state.json')

class GhostBoard(pingo.Board):

    def __init__(self):
        super(GhostBoard, self).__init__()

        pins = set([
            pingo.GroundPin(self, 1),
            pingo.VddPin(self, 2, 5.0),
            pingo.DigitalPin(self, 7),
            pingo.DigitalPin(self, 13),
        ])

        self.add_pins(pins)

    def cleanup(self):
        print('GhostBoard: cleaning up.')

    def _set_pin_mode(self, pin, mode):
        print('GhostBoard: %r mode -> %s' % (pin, mode))

    def _set_pin_state(self, pin, state):
        print('GhostBoard: %r state -> %s' % (pin, state))
        _state = 1 if state == pingo.HIGH else 0
        with open(PINS_STATE_FILEPATH, 'r') as fp:
            pins_state = json.load(fp)
            pins_state[str(pin.location)] = _state

        with open(PINS_STATE_FILEPATH, 'w') as fp:
            json.dump(pins_state, fp, indent=4)

    def _get_pin_state(self, pin):
        with open(PINS_STATE_FILEPATH, 'r') as fp:
            pins_state = json.load(fp)
            state = pins_state[str(pin.location)]
        return state
