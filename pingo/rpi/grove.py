import pingo

grovepi = None


class GrovePi(pingo.Board, pingo.AnalogInputCapable, pingo.PwmOutputCapable):

    def __init__(self):
        global grovepi
        try:
            import grovepi as grovepi  # noqa
        except ImportError:
            raise ImportError('pingo.rpi.GrovePi requires grovepi installed')

        super(GrovePi, self).__init__()

        # location: gpio_id
        self.ANALOG_PINS = {'A0': 14, 'A1': 15, 'A2': 16, 'A3': 17}

        self.PIN_MODES = {
            pingo.IN: 'INPUT',
            pingo.OUT: 'OUTPUT'
        }

        self.PIN_STATES = {
            pingo.HIGH: 1,
            pingo.LOW: 0
        }

        pwm_pins = [3, 5, 6]
        digital_pins = [0, 1, 2, 4, 7, 8, 9]

        self._add_pins(
            [pingo.PwmPin(self, location)
                for location in pwm_pins] +

            [pingo.DigitalPin(self, location)
                for location in digital_pins] +

            [pingo.AnalogPin(self, location, 10, gpio_id)
                for location, gpio_id in self.ANALOG_PINS.items()]
        )

    def _set_digital_mode(self, pin, mode):
        grovepi.pinMode(pin.location, self.PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        grovepi.digitalWrite(pin.location, self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        return pingo.LOW if grovepi.digitalRead(pin.location) == 0 else pingo.HIGH

    def _get_pin_value(self, pin):
        return (grovepi.analogRead(self.ANALOG_PINS[pin.location]) / 10.23)

    def _set_analog_mode(self, pin, mode):
        grovepi.pinMode(self.ANALOG_PINS[pin.location], 'INPUT')

    def _set_pwm_mode(self, pin, mode):
        grovepi.pinMode(pin.location, 'OUTPUT')

    def _set_pwm_frequency(self, pin, value):
        raise NotImplementedError

    def _set_pwm_duty_cycle(self, pin, value):
        grovepi.analogWrite(pin.location, int(value * 2.55))
