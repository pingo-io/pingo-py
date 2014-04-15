from pingo.board import Board
from pingo.board import DigitalPin, GroundPin, VddPin

class GhostBoard(Board):

    def __init__(self):

        pins = [
            GroundPin(self, 1),
            VddPin(self, 2, 5.0),
            DigitalPin(self, 13),
        ]

        self.add_pins(pins)

    def _set_pin_mode(self, pin, mode):
        pass

    def _set_pin_state(self, pin, state):
        pass

    def cleanup(self):
        print('GhostBoard: cleaning up.')
