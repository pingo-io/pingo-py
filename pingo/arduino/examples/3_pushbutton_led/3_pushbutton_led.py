"""
3 Pushbutton 3 led.

The led comes on when you press the button.

Connections example found on ./3_button.png

"""
# -*- coding: utf-8 -*-
import pingo
import sys


try:
    print("Loading board...")
    board = pingo.detect.get_board()
    print("Its ok...")
    led_pin1 = board.pins[13]
    led_pin1.mode = pingo.OUT
    led_pin2 = board.pins[12]
    led_pin2.mode = pingo.OUT
    led_pin3 = board.pins[11]
    led_pin3.mode = pingo.OUT
    button_pin1 = board.pins[2]
    button_pin1.mode = pingo.IN
    button_pin2 = board.pins[3]
    button_pin2.mode = pingo.IN
    button_pin3 = board.pins[4]
    button_pin3.mode = pingo.IN
except Exception as e:
    print("Error on get_board: {}".format(e))
    sys.exit(1)

while True:
    if button_pin1.state == pingo.HIGH:
        led_pin1.hi()
    else:
        led_pin1.lo()
    if button_pin2.state == pingo.HIGH:
        led_pin2.hi()
    else:
        led_pin2.lo()
    if button_pin3.state == pingo.HIGH:
        led_pin3.hi()
    else:
        led_pin3.lo()
