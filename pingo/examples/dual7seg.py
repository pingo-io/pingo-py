from time import sleep

import pingo

# board = pingo.detect.MyBoard()       # auto-detect board
galileo = pingo.galileo.Galileo2()     # explicit board selection
arduino = pingo.arduino.get_arduino()  # get Arduino via serial

galileo_pins = galileo.select_pins(range(8, 14) + [7])
arduino_pins = arduino.select_pins(range(8, 14) + [7])

galileo_d7s = pingo.parts.led.SevenSegments(*galileo_pins)
arduino_d7s = pingo.parts.led.SevenSegments(*arduino_pins)

displays = [galileo_d7s, arduino_d7s]

while True:
    for i in range(16):
        display = displays[i % 2]
        display.digit = i
        sleep(.5)
