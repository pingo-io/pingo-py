"""Blink an LED on a remote Arduino

This script assumes:

- this computer is connected to an Arduino on port ``/dev/tty.usbmodemfa1341``
- the Arduino is running the Examples->Firmata->StandardFirmata sketch

"""

import time
import pingo
from pingo import Mode

ard = pingo.arduino.ArduinoFirmata('/dev/tty.usbmodemfa1341')
print('Connected to: %s' % ard)
led = ard.pins[13]
led.mode = Mode.OUT

while True:
    led.toggle()
    time.sleep(.1)
