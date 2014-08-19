"""
Arduino coding dojo script for the XXL panel
"""

import pingo
import time

ard = pingo.arduino.get_arduino()
print '*' * 60

segments = [
    11, # A
    10, # B
     8, # C
     7, # D
     6, # E
    12, # F
    # 13, # G
]

for seg in segments:
    pin = ard.pins[seg]
    pin.mode = pingo.OUT
    pin.low()

pot = ard.pins['A0']
pot.mode = pingo.IN

while True:
    for seg in segments:
        pin = ard.pins[seg]
        pin.high()
        delay = pot.ratio() + 0.01  # add 0.01s delay for communication
        print '%0.3f' % delay
        time.sleep(delay)
        pin.low()


