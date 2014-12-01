import pingo

board = pingo.detect.MyBoard()

a_led = pingo.parts.Led(board.pins[13])
a_led.blink(0)  # times=0 means "forever"

raw_input('Hit <ENTER> to stop blinking')
a_led.stop()
