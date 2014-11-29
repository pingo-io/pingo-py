import pingo

mraa = None

class Galileo2(pingo.Board, pingo.AnalogInputCapable, pingo.PwmOutputCapable):

    def __init__(self):
        global mraa
        try:
            import mraa as mraa
        except ImportError:
            raise ImportError(
                'pingo.galileo.Galileo2 requires mraa installed')

        super(Galileo2, self).__init__()

        self.PIN_MODES = {
            pingo.IN: mraa.DIR_IN,
            pingo.OUT: mraa.DIR_OUT,
        }

        self.PIN_STATES = {
            pingo.HIGH: 1,
            pingo.LOW: 0,
        }

        self._add_pins(
            [pingo.PwmPin(self, location)
                for location in [3, 5, 6, 9, 10, 11, 13]] +

            [pingo.DigitalPin(self, location)
                for location in [1, 2, 4, 7 , 8, 12]] +

            [pingo.AnalogPin(self, 'A' + location, 12)
                for location in '012345']
        )

        self.mraa_pins = {
            location: mraa.Gpio(location)
            for location in range(1, 14)
        }

        self.mraa_analogs = {
            'A' + location: mraa.Aio(int(location))
            for location in '012345'
        }

        self.mraa_pwms = {
            location: mraa.Pwm(location)
            for location in [3, 5, 6, 9, 10, 11, 13]
        }

    def _set_pin_mode(self, pin, mode):
        if pin.mode == pingo.PWM:
            self.mraa_pwms[pin.location].enable(False)
        self.mraa_pins[pin.location].dir(self.PIN_MODES[mode])

    def _set_analog_mode(self, pin, mode):
        pass

    def _set_pwm_mode(self, pin, mode):
        self.mraa_pwms[pin.location].enable(True)

    def _set_pin_state(self, pin, state):
        self.mraa_pins[pin.location].write(self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        value = self.mraa_pins[pin.location].read()
        return pingo.HIGH if value == 1 else pingo.LOW

    def _get_pin_value(self, pin):
        return self.mraa_analogs[pin.location].read()

    def _get_pwm_duty_cycle(self, pin):
        return 0 # TODO

    def _set_pwm_duty_cycle(self, pin, value):
        self.mraa_pwms[pin.location].write(value)

