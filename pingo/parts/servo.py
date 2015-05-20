import pingo
from pingo.board import ArgumentOutOfRange


class Servo(object):

    def __init__(self, pin, start_position=90):
        pin.mode = pingo.PWM
        pin.frequency = 50
        self.pin = pin
        self.move(start_position)

    def move(self, position):
        if not 0 <= position <= 180:
            raise ArgumentOutOfRange()
        self.pin.value = float(position) * (12.5 - 2.5) / (180.0) + 2.5



