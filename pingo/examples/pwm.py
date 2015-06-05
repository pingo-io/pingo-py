"""
Using PWM on pin #6 to dim a LED

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
    led.value = 1.0 / p
    time.sleep(0.05)
