from pingo.board import Board, DigitalPin, GroundPin, VddPin

DIGITAL_PIN_MAP = {
    3: 2, 5: 3, 7: 4, 8: 14, 10: 15, 11: 17, 12: 18, 13: 27, 15: 22,
    16: 23, 18: 24, 19: 10, 21: 9, 22: 25, 23: 11, 24: 8, 26: 7,
}
GROUND_PINS = (6, 9, 14, 20, 25)

class RaspberryPi(Board):

    def __init__(self):
        pins = {
           1 : VddPin(self, "3.3V"),
           2 : VddPin(self, "5V"),
           4 : VddPin(self, "5V"),
          17 : VddPin(self, "3.3V"),
        }
        pins.update({key: DigitalPin(self, log_id)
                for key, log_id in DIGITAL_PIN_MAP.items()})
        pins.update({key: GroundPin(self) for key in GROUND_PINS})
        self.add_pins(pins)

    def set_pin_mode(self, pin, mode):
        pass
