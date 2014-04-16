#!/usr/bin/env python
# coding: utf-8

# MIT Licensed
# http://opensource.org/licenses/MIT

# UDOO pin mapping
# http://www.udoo.org/ProjectsAndTutorials/linux-gpio-manipulation/
led_dir = "/sys/class/gpio/gpio40/" # Arduino pin #13
led_pin = led_dir + "value"
led_mode = led_dir + "direction"

with open(led_mode, "wb") as f:
    f.write("out")

# argv[1] = '0' -> set pin to low
#           '1' -> set pin to high

with open(led_pin, "wb") as f:
    f.write(__import__("sys").argv[1])

"""
Participantes!

Danilo J. S. Bellini
Estevão U. P. Vieira
Lucas  S. Simões
Thiago M. Sanches
Paulo R. O. Castro

AEEEW!!!! =D
"""
