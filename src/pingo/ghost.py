from pingo.board import Board, DigitalPin

class GhostBoard(Board):

    def __init__(self):

		self.add_pins([(13, DigitalPin(self, 13))])

    def set_pin_mode(self, pin, mode):
        pass

    def set_pin_state(self, pin, state):
        pass
