"""Blink an LED on a remote Arduino

This script assumes:

- this computer is connected to an Arduino
- the Arduino is running the Examples->Firmata->StandardFirmata sketch

"""

import time
import pingo

ard = pingo.arduino.get_arduino()
print('Connected to: %s' % ard)
led = ard.pins[13]
led.mode = pingo.OUT

while True:
    led.toggle()
    time.sleep(.5)
