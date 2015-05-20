import pingo
from pingo.board import ArgumentOutOfRange


class Servo(object):

    def __init__(self, pin):
        pin.mode = pingo.PWM
        pin.frequency = 50
        self.pin = pin
        # Percent of dutycycle that represents zero
        # Default: 2.5% ~ 0.5ms pulse @ 50Hz
        self._botton_end = 2.5
        # Percent of dutycycle that represents 180
        # Default: 12.5% ~ 2.5ms pulse @ 50Hz
        self._top_end = 12.5

    def move(self, position):
        if not 0 <= position <= 180:
            raise ArgumentOutOfRange()
        pmin, pmax = self._botton_end, self._top_end
        self.pin.value = float(position) * (pmax - pmin) / (180.0) + pmin
