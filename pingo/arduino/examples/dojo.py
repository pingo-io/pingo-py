import sys
from time import sleep

import pingo

#######
try:
    serial_port = sys.argv[1]
except IndexError:
    try:
        ard = pingo.arduino.get_arduino()
    except LookupError:
        print('Serial port auto-detect failed.')
        print('Usage: %s <serial-port>' % sys.argv[0])
        raise SystemExit
else:
    ard = pingo.arduino.ArduinoFirmata(serial_port)

print('Found: %r' % ard)
#######

pins = [ard.pins[n] for n in (6, 7, 8, 13, 12, 11, 10, 13)]

for pin in pins:
    pin.mode = pingo.OUT

DELAY = .1

prev_pin = None

while True:
    for pin in pins:
        pin.high()
        sleep(DELAY)
        if prev_pin:
            prev_pin.low()
        prev_pin = pin
