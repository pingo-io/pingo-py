from pingo.board import Board, DigitalPin, GroundPin, VddPin

class RaspberryPi(Board):

    def __init__(self):
        self.add_pins({
           1 : VddPin(self, "3.3V"),
           2 : VddPin(self, "5V"),
           3 : DigitalPin(self, 2),
           4 : VddPin(self, "5V"),
           5 : DigitalPin(self, 3),
           6 : GroundPin(self),
           7 : DigitalPin(self, 4),
           8 : DigitalPin(self, 14),
           9 : GroundPin(self),
          10 : DigitalPin(self, 15),
          11 : DigitalPin(self, 17),
          12 : DigitalPin(self, 18),
          13 : DigitalPin(self, 27),
          14 : GroundPin(self),
          15 : DigitalPin(self, 22),
          16 : DigitalPin(self, 23),
          17 : VddPin(self, "3.3V"),
          18 : DigitalPin(self, 24),
          19 : DigitalPin(self, 10),
          20 : GroundPin(self),
          21 : DigitalPin(self, 9),
          22 : DigitalPin(self, 25),
          23 : DigitalPin(self, 11),
          24 : DigitalPin(self, 8),
          25 : GroundPin(self),
          26 : DigitalPin(self, 7),
        })
