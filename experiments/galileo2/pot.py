from time import sleep
import mraa

MAX_VALUE = 2. ** 12 -1

pot = mraa.Aio(0)
while 1:
    print '#' * int(pot.read()/MAX_VALUE * 70)
    sleep(.05)
