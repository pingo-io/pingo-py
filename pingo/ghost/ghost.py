import pingo

class GhostBoard(pingo.Board):

    def __init__(self):
        super(GhostBoard, self).__init__()

        pins = [
            pingo.GroundPin(self, 1),
            pingo.VddPin(self, 2, 5.0),
            pingo.DigitalPin(self, 13),
        ]

        self.add_pins(pins)

    def cleanup(self):
        print('GhostBoard: cleaning up.')

    def _set_pin_mode(self, pin, mode):
        pass

    def _set_pin_state(self, pin, state):
        pass

    def _get_pin_state(self, pin):
        return pingo.LOW
