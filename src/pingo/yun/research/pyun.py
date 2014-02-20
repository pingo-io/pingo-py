# coding: utf-8

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

import urllib
import time

INPUT = 'input'
OUTPUT = 'output'
HIGH = 1
LOW = 0
PINS = range(0, 14)

class YunBridge(object):

    def __init__(self, host, verbose=False):
        self.host = host
        self.base_url = 'http://%s/arduino/' % host
        self.verbose = verbose
        for pin in PINS:
            self.digitalWrite(pin, 0)
            self.pinMode(pin, INPUT)

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
        if mode not in [INPUT, OUTPUT]:
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
