import time

import pingo

# connector_p1_location: gpio_id
DIGITAL_PIN_MAP = {
    3: 2,
    5: 3,
    7: 4,
    8: 14,
    10: 15,
    11: 17,
    12: 18,
    13: 27,
    15: 22,
    16: 23,
    18: 24,
    19: 10,
    21: 9,
    22: 25,
    23: 11,
    24: 8,
    26: 7,
}

class RaspberryPi(pingo.Board):

    def __init__(self):
        global GPIO
        try:
            import RPi.GPIO as GPIO
        except ImportError:
            raise SystemExit('pingo.rpi requires RPi.GPIO installed')

        super(RaspberryPi, self).__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

        pins = [
                    pingo.VddPin(self, 1, 3.3),
                    pingo.VddPin(self, 2, 5.0),
                    pingo.VddPin(self, 4, 5.0),
                    pingo.VddPin(self, 17, 3.3),
        ]

        pins += [pingo.GroundPin(self, n) for n in [6, 9, 14, 20, 25]]

        pins += [pingo.DigitalPin(self, location, gpio_id)
                    for location, gpio_id in DIGITAL_PIN_MAP.items()]

        self.add_pins(pins)

    def cleanup(self):
        for pin in self.pins.values():
            if hasattr(pin, 'enabled') and pin.enabled:
                GPIO.cleanup(int(pin.gpio_id))
                pin.enabled = False

    def _set_pin_mode(self, pin, mode):
        rpi_mode = GPIO.IN if mode == pingo.INPUT else GPIO.OUT
        GPIO.setup(int(pin.gpio_id), rpi_mode)

    def _set_pin_state(self, pin, state):
        rpi_state = GPIO.HIGH if state == pingo.HIGH else GPIO.LOW
        GPIO.output(int(pin.gpio_id), rpi_state)

