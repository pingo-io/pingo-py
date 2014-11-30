import pingo
import time

galileo = pingo.detect.MyBoard()
arduino = pingo.arduino.get_arduino()

pot_galileo = galileo.pins['A0']
pot_galileo.mode = pingo.ANALOG

pot_arduino = arduino.pins['A0']
pot_arduino.mode = pingo.ANALOG


def bar(pin1, pin2):
    bar1 = ('*' * int(pin1.ratio() * 40)).ljust(40)
    bar2 = ('*' * int(pin2.ratio() * 40)).rjust(40)
    print bar2 + bar1

while True:
    bar(pot_galileo, pot_arduino)
    time.sleep(0.05)
