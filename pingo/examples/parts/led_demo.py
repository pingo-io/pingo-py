import pingo
import time

board = pingo.detect.MyBoard()

a_led = pingo.parts.Led(board.pins[13])
a_led.blink(3)

b_led = pingo.parts.Led(board.pins[12])
b_led.blink(6, .6, .2)

while any([a_led.blinking, b_led.blinking]):
    a_state = '*A*' if a_led.lit else ' a '
    b_state = '*B*' if b_led.lit else ' b '

    print time.strftime('%H:%M:%S'), a_state, b_state
    time.sleep(.1)
