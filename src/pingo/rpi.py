from board import Board, DigitalPin

class RaspberryPi(Board):

    def __init__(self):
        self.pins = {11:DigitalPin(11)}
