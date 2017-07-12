import time
import pingo
from pingo import Mode

board = pingo.galileo.Galileo2()

pot = board.pins['A0']
pot.mode = Mode.ANALOG


def bar(pin):
    print("*" * int(pin.ratio() * 70))

while True:
    bar(pot)
    time.sleep(0.05)
