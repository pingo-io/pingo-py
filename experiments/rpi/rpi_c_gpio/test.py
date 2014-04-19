import rpi
import time

b = rpi.cRaspberryPi()

for pin in b.pins.values():
    print pin

p = b.pins[3]
p.set_mode(rpi.OUT)
while 1:
    p.high()
    time.sleep(1)
    p.low()
    time.sleep(1)

