from pingo.board import Board, DigitalPin

class GhostBoard(Board):

    def __init__(self):
		self.add_pins([(13, DigitalPin(13))])
