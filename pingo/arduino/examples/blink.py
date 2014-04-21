import sys
from time import sleep

import pingo

try:
    serial_port = sys.argv[1]
except IndexError:
    print('Usage: %s <serial-port>' % sys.argv[0])
    raise SystemExit

print('Connecting via: %r' % serial_port)
ard = pingo.arduino.ArduinoFirmata(serial_port)
print('Found: %r' % ard)

led_pin = ard.pins[13]
led_pin.mode = pingo.OUT

while True:
    led_pin.high()
    sleep(.5)
    led_pin.low()
    sleep(.5)
