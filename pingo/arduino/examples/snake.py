import sys
import atexit
import platform
from time import sleep

import pingo

#######
try:
    serial_port = sys.argv[1]
except IndexError:
    serial_port = pingo.detect.detect._find_arduino_dev(platform.system())
    if not serial_port:
        print('Serial port auto-detect failed.')
        print('Usage: %s <serial-port>' % sys.argv[0])
        raise SystemExit

print('Connecting via: %r' % serial_port)
ard = pingo.arduino.ArduinoFirmata(serial_port)
print('Found: %r' % ard)
#######

def apagar_todos():
    for pin in pins:
        pin.low()
        print pin, pin.state

atexit.register(apagar_todos)

pins = [ard.pins[n] for n in (6, 7, 8, 10, 11, 12, 13)]

for pin in pins:
    pin.mode = pingo.OUT

DELAY = 1

while True:
    for pin in pins:
        pin.high()
        print pin, pin.state
        sleep(DELAY)
        pin.low()
        print pin, pin.state
