import pingo
import time

this = pingo.detect.MyBoard()
that = pingo.arduino.get_arduino()

pot_this = this.pins['A0']
pot_this.mode = pingo.ANALOG

pot_that = that.pins['A0']
pot_that.mode = pingo.ANALOG


def bar(pin1, pin2):
    bar1 = ('*' * int(pin1.ratio() * 40)).ljust(40)
    bar2 = ('*' * int(pin2.ratio() * 40)).rjust(40)
    print bar1 + bar2

while True:
    bar(pot_this, pot_that)
    time.sleep(0.05)
