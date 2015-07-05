"""
Using PWM on pin #6 to dim a LED

"""

from pprint import pprint
import pingo
import time

#board = pingo.detect.get_board()
board = pingo.arduino.get_arduino()

from IPython import embed; embed()

led = board.pins[10]
led.mode = pingo.PWM

pprint(board.pins, indent=4, width=1)

led.value = 50

raw_input()
