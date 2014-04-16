import pingo

rpi = pingo.rpi.RaspberryPi()

fmt = '{:>22s} {:2d} {:<2d} {}'
for loc1, pin1 in sorted(rpi.pins.items())[::2]:
    loc2 = loc1 + 1
    pin2 = rpi.pins[loc2]
    print fmt.format(pin1, loc1, loc2, pin2)
    
