from pyfirmata import Arduino
from time import sleep
import sys

board = Arduino(sys.argv[1])

while True:
    board.digital[13].write(1)
    sleep(.5)
    board.digital[13].write(0)
    sleep(.5)
