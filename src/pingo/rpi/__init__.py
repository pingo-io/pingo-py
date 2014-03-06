from pingo.board import Board, DigitalPin

class RaspberryPi(Board):

    def __init__(self):
        self.pins = {
           1 : DigitalPin(11),
           2 : DigitalPin(11),
           3 : DigitalPin(11),
           4 : DigitalPin(11),
           5 : DigitalPin(11),
           6 : DigitalPin(11),
           7 : DigitalPin(11),
           8 : DigitalPin(11),
           9 : DigitalPin(11),
          11 : DigitalPin(11),
          12 : DigitalPin(11),
          13 : DigitalPin(11),
          14 : DigitalPin(11),
          15 : DigitalPin(11),
          16 : DigitalPin(11),
          17 : DigitalPin(11),
          18 : DigitalPin(11),
          19 : DigitalPin(11),
          21 : DigitalPin(11),
          22 : DigitalPin(11),
          23 : DigitalPin(11),
          24 : DigitalPin(11),
          25 : DigitalPin(11),
          26 : DigitalPin(11),
          27 : DigitalPin(11),
          28 : DigitalPin(11),
        }
