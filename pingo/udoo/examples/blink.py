import pingo
from time import sleep

board = pingo.udoo.Udoo()
led_pin = board.pins[13]
led_pin.mode = pingo.OUT

while True:
    led_pin.on()
    print '%r -> %r' % (led_pin, led_pin.state)
    sleep(1)
    led_pin.off()
    print '%r -> %r' % (led_pin, led_pin.state)
    sleep(1)
