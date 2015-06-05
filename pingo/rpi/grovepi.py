import pingo

class GrovePi(pingo.Board):

    def __init__(self):

        try:
            import grovepi
        except ImportError:
            raise ImportError('pingo.rpi.GrovePi requires grovepi installed')

        super(GrovePi, self).__init__()

        self.PIN_MODES = {
            pingo.IN: 'INPUT',
            pingo.OUT: 'OUTPUT'
        }

        self.PIN_STATES = {
            pingo.HIGH: 1,
            pingo.LOW: 0
        }

        pwm_pins = [3, 5, 6]
        digital_pins = ['serial_d0', 'serial_d1', 2, 4, 7, 8, 9]

        self._add_pins(
            [pingo.PwmPin(self, location)
                for location in pwm_pins] +

            [pingo.DigitalPin(self, location)
                for location in digital_pins] +

            [pingo.AnalogPin(self, 'A' + location, 12)
                for location in '0123']
        )

        def _set_digital_mode(self, pin, mode):
            grovepi.pinMode(pin, self.PIN_MODES[mode])

        def _set_pin_state(self, pin, state):
            grovepi.digitalWrite(pin, self.PIN_STATES)

        def _get_pin_state(self, pin):
            return pingo.LOW if grovepi.digitalRead(pin) == 0 else pingo.HIGH

        def _get_pin_value(self, pin):
            return (grovepi.analogRead(pin) / 1023)

        def _set_analog_mode(self, pin):
            grovepi.pinMode(pin, 'INPUT')