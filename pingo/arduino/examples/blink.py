from time import sleep

import pingo

ard = pingo.arduino.get_arduino()

led_pin = ard.pins[10]
led_pin.mode = pingo.OUT

while True:
    led_pin.hi()
    print(led_pin.state)
    sleep(1)
    led_pin.low()
    print(led_pin.state)
    sleep(1)
