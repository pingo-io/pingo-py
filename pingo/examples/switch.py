"""

This example is controlled by the switch in 3
It shows 1 if its closed, or 0 if its open. 
"""

import pingo
import time

board = pingo.detect.MyBoard()

display_pins = [board.pins[i] for i in range(8, 14) + [7]]
seg_display = pingo.parts.led.SevenSegments(*display_pins)

def show_f():
    global seg_display
    seg_display.digit = 0xF
    print 'Fechado'  # Closed    

def show_a():
    global seg_display
    seg_display.digit = 0xA    
    print 'Aberto'  # Open    

pin_sw = board.pins[3]
my_switch = pingo.parts.Switch(pin_sw)
my_switch.set_callback_down(show_a)
my_switch.set_callback_up(show_f)

seg_display.digit = 8    

my_switch.start()

try:
    while True:
       time.sleep(.5)
       print pin_sw.state
except:
    my_switch.stop()
else:
    my_switch.stop()
