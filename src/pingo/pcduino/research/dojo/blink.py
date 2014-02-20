#!/usr/bin/env python

"""
Blink:
piscar o ponto decimal no display de 7 segmentos do circuito 'Dojo com pcDuino'
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins

import time

GPIO_PATH = '/sys/devices/virtual/misc/gpio/'
GPIO_MODE_PATH = GPIO_PATH + 'mode/'
GPIO_DATA_PATH = GPIO_PATH + 'pin/'

OUTPUT_MODE = "1"
PONTO_DECIMAL = 3
ON = "1"
OFF = "0"

DEBUG = True

def setup():
    for i in range(8):
        with open(GPIO_MODE_PATH+'gpio%s'%i, 'w') as f:
            f.write(OUTPUT_MODE)
        with open(GPIO_DATA_PATH+'gpio%s'%i, 'w') as f:
            f.write(OFF)

def set(pin, value):
    with open(GPIO_DATA_PATH+'gpio%s'%pin, 'w') as f:
        f.write(str(value))

pin = PONTO_DECIMAL
setup()
while True:
    set(pin, ON)
    print pin, 'ON'
    time.sleep(1)
    set(pin, OFF)
    print pin, 'OFF'
    time.sleep(1)
