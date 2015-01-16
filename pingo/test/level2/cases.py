import pingo

'''
In order to use this set of cases, it is necessary to set
the following attributes on your TestCase setUp:
    self.pwm_pin_number = 0
'''


class PwmBasics(object):

    def test_dot50_duty_cycle(self):
        pin = self.board.pins[self.pwm_pin_number]
        pin.mode = pingo.PWM
        pin.value = 0.50

        _duty_cycle = pin.value
        # print "Value Read: ", _duty_cycle

        assert 0.49 <= _duty_cycle <= 0.51

    def test_frequency(self):
        pin = self.board.pins[self.pwm_pin_number]
        pin.mode = pingo.PWM
        pin.frequency = 440

        _frequency = pin.frequency
        assert 439 <= _frequency <= 441


class PwmExceptions(object):

    def test_wrong_analog_mode(self):
        pin = self.board.pins[self.pwm_pin_number]
        with self.assertRaises(pingo.ModeNotSuported):
            pin.mode = pingo.ANALOG

    def test_wrong_read_state(self):
        pin = self.board.pins[self.pwm_pin_number]
        pin.mode = pingo.PWM

        with self.assertRaises(pingo.WrongPinMode):
            pin.state

        with self.assertRaises(pingo.WrongPinMode):
            pin.low()
