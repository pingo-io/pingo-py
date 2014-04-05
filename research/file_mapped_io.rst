

=======
pcDuino
=======

source:
https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins

digital
=======

set mode
--------

INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"  # INPUT, with a pull-up resistor
filemode = "r+"

/sys/devices/virtual/misc/gpio/mode/gpio{gpio_id:d}

analog
======

A0 and A1 are six-bit inputs, returning a value from 0-63 over a range from 0-2V; A2-A5 are 12-bit inputs operating across the full 3.3V range.

/proc/adc{gpio_id:d}


