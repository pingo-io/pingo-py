"""
Utility to map Arduino pins connected to a 7-segment display
"""

import pingo

ard = pingo.arduino.get_arduino()
print '*' * 60
segs = {}

for i in range(14):
    pin = ard.pins[i]
    pin.mode = pingo.OUT
    pin.hi()
    seg = raw_input('Pin %s -> segment: ' % i).strip()
    if seg:
        segs[seg] = i
    pin.low()

for seg, pin in sorted(segs.items()):
    print '%s, # %s' % (pin, seg)
