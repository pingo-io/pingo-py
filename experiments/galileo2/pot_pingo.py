from time import sleep
import pingo

MAX_VALUE = 2. ** 12 -1

g = pingo.detect.MyBoard()
pot = g.pins['A0']

while 1:
    print '#' * int(pot.value/MAX_VALUE * 70)
    sleep(.05)
