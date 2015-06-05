"""

This example is controlled by the knob in A0
It shows the level of power on the display
and lights a PWM Led on 6 (or the dicimal point)

"""

from pprint import pprint
import pingo
import time

board = pingo.detect.get_board()
print board


led = board.pins[6]
led.mode = pingo.PWM

pprint(board.pins, indent=4, width=1)

for p in range(1, 100):
    led.value = 1.0/p
    time.sleep(0.05)
