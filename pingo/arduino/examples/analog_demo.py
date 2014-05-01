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

pin = ard.pins['A0']

while True:
    if pin.value is not None:
        sleep(.02)
        print '%0.4f' % pin.value, int(70 * pin.value) * '*'
