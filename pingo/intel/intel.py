import pingo

mraa = None


class BaseMraa(pingo.Board, pingo.AnalogInputCapable, pingo.PwmOutputCapable):

    _import_error_msg = 'pingo.intel.BaseMraa requires mraa installed'

    def __init__(self):
        global mraa
        try:
            import mraa as mraa
        except ImportError:
            raise ImportError(self._import_error_msg)

        super(Galileo2, self).__init__()

        self.PIN_MODES = {
            pingo.IN: mraa.DIR_IN,
            pingo.OUT: mraa.DIR_OUT,
        }

        self.PIN_STATES = {
            pingo.HIGH: 1,
            pingo.LOW: 0,
        }

        pwm_pin_numbers = [3, 5, 6, 9, 10, 11, 13]
        digital_pin_numbers = [1, 2, 4, 7, 8, 12]

        self._add_pins(
            [pingo.PwmPin(self, location)
                for location in pwm_pin_numbers] +

            [pingo.DigitalPin(self, location)
                for location in digital_pin_numbers] +

            [pingo.AnalogPin(self, 'A' + location, 12)
                for location in '012345']
        )

        self.mraa_pins, self.mraa_analogs, self.mraa_pwms = {}, {}, {}

    def _set_digital_mode(self, pin, mode):
        if pin.mode == pingo.PWM:
            self.mraa_pwms[pin.location].enable(False)
        self.mraa_pins[pin.location] = mraa.Gpio(pin.location)
        self.mraa_pins[pin.location].dir(self.PIN_MODES[mode])

    def _set_analog_mode(self, pin, mode):
        mraa_id = int(pin.location[1])
        self.mraa_analogs[pin.location] = mraa.Aio(mraa_id)

    def _set_pwm_mode(self, pin, mode):
        if pin.mode == pingo.IN:
            self.mraa_pins[pin.location].dir(mraa.DIR_OUT)
        self.mraa_pwms[pin.location] = mraa.Pwm(pin.location)
        self.mraa_pwms[pin.location].enable(True)

    def _set_pin_state(self, pin, state):
        self.mraa_pins[pin.location].write(self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        value = self.mraa_pins[pin.location].read()
        return pingo.HIGH if value == 1 else pingo.LOW

    def _get_pin_value(self, pin):
        return self.mraa_analogs[pin.location].read()

    def _set_pwm_duty_cycle(self, pin, value):
        self.mraa_pwms[pin.location].write(value)

    def _set_pwm_frequency(self, pin, value):
        raise NotImplementedError


class Galileo2(BaseMraa):
    _import_error_msg = 'pingo.intel.Galileo2 requires mraa installed'


class Edison(BaseMraa):
    _import_error_msg = 'pingo.intel.Edison requires mraa installed'
