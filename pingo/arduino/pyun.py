# coding: utf-8

import urllib
import time

import pingo

# INPUT = 'input'
# OUTPUT = 'output'
# HIGH = 1
# LOW = 0
# PINS = range(0, 14)


class YunBridge(object):

    """
    Pyun: Python interface to Arduino Yún via HTTP to Bridge sketch

    WARNING: this requires the Bridge sketch running on the Arduino.

    About Bridge:
    http://arduino.cc/en/Tutorial/Bridge

    Bridge REST cheat-sheet:

     * "/arduino/digital/13"     -> digitalRead(13)
     * "/arduino/digital/13/1"   -> digitalWrite(13, HIGH)
     * "/arduino/analog/2/123"   -> analogWrite(2, 123)
     * "/arduino/analog/2"       -> analogRead(2)
     * "/arduino/mode/13/input"  -> pinMode(13, INPUT)
     * "/arduino/mode/13/output" -> pinMode(13, OUTPUT)
    """

    def __init__(self, host, verbose=False):
        self.host = host
        self.base_url = 'http://%s/arduino/' % host
        self.verbose = verbose
        # for pin in PINS:
        #     self.digitalWrite(pin, 0)
        #     self.pinMode(pin, INPUT)

    def makeURL(self, command, pin, *args):
        rest_args = '/'.join(str(x) for x in args)
        if rest_args:
            url = self.base_url + '%s/%d/%s' % (command, pin, rest_args)
        else:
            url = self.base_url + '%s/%d' % (command, pin)
        if self.verbose:
            print '[YunBridge] url: ', url
        return url

    def get(self, command, pin, *args):
        url = self.makeURL(command, pin, *args)
        res = urllib.urlopen(url).read()
        return res

    def pinMode(self, pin, mode):
        mode = mode.lower()
        if mode not in ['input', 'output']:
            raise TypeError('mode should be "input" or "output" ')
        res = self.get('mode', pin, mode)
        # Pin D13 configured as INPUT!
        return res.split()[-1][:-1].lower()

    def digitalRead(self, pin):
        res = self.get('digital', pin)
        # Pin D13 set to 1
        return int(res.split()[-1])

    def digitalWrite(self, pin, value):
        res = self.get('digital', pin, value)
        # Pin D13 set to 0
        return int(res.split()[-1])

    def analogRead(self, pin):
        res = self.get('analog', pin)
        # Pin A5 reads analog 185
        return int(res.split()[-1])

    def delay(self, ms):
        seconds = float(ms) / 1000
        time.sleep(seconds)


class ArduinoYun(pingo.Board, pingo.AnalogInputCapable, pingo.PwmOutputCapable):

    def __init__(self, host, verbose=False):

        super(ArduinoYun, self).__init__()

        self.yun = YunBridge(host, verbose)

        self.PIN_MODES = {
            pingo.IN: 'input',
            pingo.OUT: 'output',
        }

        self.PIN_STATES = {
            pingo.HIGH: 1,
            pingo.LOW: 0,
        }

        pwm_pin_numbers = [3, 5, 6, 9, 10, 11, 13]
        digital_pin_numbers = [0, 1, 2, 4, 7, 8, 12]

        self._add_pins(
            [pingo.PwmPin(self, location)
                for location in pwm_pin_numbers] +

            [pingo.DigitalPin(self, location)
                for location in digital_pin_numbers] +

            [pingo.AnalogPin(self, 'A' + location, 10)
                for location in '012345']
        )

    def _set_pin_mode(self, pin, mode):
        if mode in [pingo.OUT, pingo.ANALOG]:
            self.yun.pinMode('input')
        else:
            self.yum.pinMode('output')

    def _set_analog_mode(self, pin, mode):
        self.set_pin_mode(pin, mode)

    def _set_pwm_mode(self, pin, mode):
        self.set_pin_mode(pin, mode)

    def _set_pin_state(self, pin, state):
        self.yun.digitalWrite(pin.location, self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        value = self.yun.digitalRead(pin.location)
        return pingo.HIGH if value == 1 else pingo.LOW

    def _get_pin_value(self, pin):
        return self.yun.digitalRead(pin.location)

    def _get_pwm_duty_cycle(self, pin):
        if hasattr(pin, '_duty_cycle'):
            return pin._duty_cycle
        else:
            return 0.0

    def _set_pwm_duty_cycle(self, pin, value):
        self.yun.analogWrite(pin.location, value)
        pin._duty_cycle = value
