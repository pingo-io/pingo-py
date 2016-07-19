# Sensor input
# run: python -i sensor.py

import pingo

board = pingo.ghost.GhostBoard('foo.json')          # gets an instance of your board's driver

s_on = board.pins[9]                    # on/off switch that the user presses
s_down = board.pins[10]                 # Bottom switch
s_up = board.pins[11]                   # Top switch

s_on.mode = pingo.OUT
s_down.mode = pingo.OUT
s_up.mode = pingo.OUT

s_up.hi()
