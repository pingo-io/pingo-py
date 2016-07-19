""" Seven segment display demo using the Garoa Dojo Shield """

from time import sleep
from pingo import OUT, detect, parts

INTERVAL = 0.3

ard = detect.get_board()

display_pins = [ard.pins[i] for i in range(8, 14) + [7]]

for pin in display_pins:
    pin.mode = OUT

seg_display = parts.led.SevenSegments(*display_pins)

for num in range(16):
    seg_display.digit = num
    print('Current digit: {:x}'.format(seg_display.digit))
    sleep(INTERVAL)

for i in range(3):
    seg_display.off()
    sleep(INTERVAL)
    seg_display.on()
    sleep(INTERVAL)

seg_display.off()
