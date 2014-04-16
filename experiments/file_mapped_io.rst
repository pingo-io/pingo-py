============
Raspberry Pi
============

http://lwn.net/Articles/31185/

http://elinux.org/Rpi_Low-level_peripherals#Bash_shell_script.2C_using_sysfs.2C_part_of_the_raspbian_operating_system

www.cs.unca.edu/~bruce/Fall13/360/GPIO_Wk7.ppt

#!/bin/sh
echo 17 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio17/direction
while true
do
        echo 1 > /sys/class/gpio/gpio17/value
        sleep 1
        echo 0 > /sys/class/gpio/gpio17/value
        sleep 1
done

Make the pin available for other applications using with the command:   echo 17 > /sys/class/gpio/unexport

http://www.raspberrypi.org/forums/viewtopic.php?f=26&t=27830
http://luketopia.net/2013/07/28/raspberry-pi-gpio-via-the-shell/
https://sites.google.com/site/semilleroadt/raspberry-pi-tutorials/gpio
http://falsinsoft.blogspot.com.br/2012/11/access-gpio-from-linux-user-space.html

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


