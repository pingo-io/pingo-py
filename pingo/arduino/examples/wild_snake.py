import sys
import atexit
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

def clear_all():
    for pin in pins:
        pin.low()

atexit.register(clear_all)

pins = [ard.pins[n] for n in (6, 7, 8, 13, 12, 11, 10, 13)]

for pin in pins:
    pin.mode = pingo.OUT

DELAY = .1

prev_pin = None

pot = ard.pins['A0']

delay = pot.value

while delay is None:
    delay = pot.value

prev_delay = delay

while True:
    for pin in pins:
        pin.high()
        delay = pot.value
        if delay is None:
            delay = prev_delay
        sleep(delay + 0.001)
        if prev_pin:
            prev_pin.low()
        prev_pin = pin
