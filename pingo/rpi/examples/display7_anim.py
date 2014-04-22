import pingo
from time import sleep

rpi = pingo.rpi.RaspberryPi()

#                 A  B   C   D   E   F  G   dp
led_locations = [11, 7, 21, 24, 26, 13, 15, 19]

pins = [rpi.pins[loc] for loc in led_locations[:6]]

for pin in pins:
    pin.mode = pingo.OUT
    pin.off()

while True:
    for pin in pins:
        pin.on()
        sleep(.04)
        pin.off()
