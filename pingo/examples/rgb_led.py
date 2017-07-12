import time

import pingo
from pingo import Mode

board = pingo.detect.get_board()

rgb = [board.pins[i] for i in (11, 13, 15)]

for pin in rgb:
    pin.mode = Mode.OUT
    pin.low()

while True:
    for pin in rgb:
        pin.low()
        print(pin, pin.state)
        time.sleep(.5)
        pin.high()
    break
