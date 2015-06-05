"""

This example is controlled by the knob in A0
It shows the level of power on the display
and lights a PWM Led on 6 (or the dicimal point)

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
