#!/usr/bin/env python
# coding: utf-8

# MIT Licensed
# http://opensource.org/licenses/MIT

# UDOO pin mapping
# http://www.udoo.org/ProjectsAndTutorials/linux-gpio-manipulation/

import time
import atexit

led_dir = "/sys/class/gpio/gpio40/" # Arduino pin #13
led_pin = led_dir + "value"
led_mode = led_dir + "direction"

with open(led_mode, "wb") as f:
    f.write("out")

# argv[1] = '0' -> set pin to low
#           '1' -> set pin to high

def set_pin(state):
    state = str(state)
    with open(led_pin, "wb") as f:
        f.write(state)

atexit.register(set_pin, 0)

def blink(delay=1):
    set_pin(1)
    time.sleep(delay)
    set_pin(0)
    time.sleep(delay)
    
if __name__=='__main__':

    import sys
    if len(sys.argv) == 2:
        delay = float(sys.argv[1])
    else:
        delay = 1  # 1s

    while True:
        blink(delay)    

"""
Participantes!

Danilo J. S. Bellini
Estevão U. P. Vieira
Lucas  S. Simões
Thiago M. Sanches
Paulo R. O. Castro

AEEEW!!!! =D
"""
