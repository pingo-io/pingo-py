### horrible hack: need to properly package and install pingo library
import sys
import os
path = os.path.abspath(__file__)
path = path[:path.rfind('pingo')]
sys.path.append(path)
### please ignore this line and all above it

import pingo
from time import sleep

board = pingo.udoo.Udoo()
led_pin = board.pins[13]
led_pin.set_mode(pingo.OUT)

while True:
    led_pin.high()
    print '%r -> %r' % (led_pin, led_pin.state)
    sleep(1)
    led_pin.low()
    print '%r -> %r' % (led_pin, led_pin.state)
    sleep(1)

