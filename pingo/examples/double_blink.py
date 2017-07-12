"""Blink an LED via the current board and another via an Arduino

This script assumes:

- ``board.pins[13]`` is a ``DigitalPin``
- ``ard.pins[13]`` is a ``DigitalPin``
- there is an LED attached to each of them

"""

import time
import pingo
from pingo import Mode

board = pingo.rpi.RaspberryPiBPlus()
local_led = board.pins[13]
local_led.mode = Mode.OUT

ard = pingo.arduino.get_arduino()
remote_led = ard.pins[13]
remote_led.mode = Mode.OUT

local_led.low()  # for an common anode RGB LED
remote_led.low()

print('LOCAL: ' + local_led.state)
print('REMOTE: ' + local_led.state)

while True:
    local_led.toggle()
    remote_led.toggle()
    print('LOCAL: ' + local_led.state)
    print('REMOTE: ' + local_led.state)
    time.sleep(.5)
