#!/usr/bin/env python

"""
Segunda versao do Dojo com pcDuino programada por Luciano Ramalho no TDC 2013
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

import time, os

GPIO_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/')
ADC_PATH = os.path.normpath('/proc/')

INPUT = "0"
OUTPUT = "1"
HIGH = "1"
LOW =  "0"

def pin_mode(pin, mode):
    with open(GPIO_PATH+'mode/gpio%s' % pin, 'w') as f:
        f.write(mode)

def digital_write(pin, value):
    with open(GPIO_PATH+'pin/gpio%s' % pin, 'w') as f:
        f.write(str(value))

def analog_read(pin):
    with open(ADC_PATH+'adc%d' % pin) as f:
        f.seek(0)
        return int(f.read(16).split(':')[1])

def setup():
    for i in range(18):
        pin_mode(i, OUTPUT)
        digital_write(i, LOW)

setup()
while True:
    for i in [0, 1, 7, 5, 4, 2]:
        digital_write(i, 1)
        delay = analog_read(5)/4096.0
        time.sleep(delay)
        digital_write(i, 0)
