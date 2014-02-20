#!/usr/bin/env python
# coding: utf-8

# MIT Licensed
# http://opensource.org/licenses/MIT

led_dir = "/sys/class/gpio/gpio40/"
led_pin = led_dir + "value"
led_mode = led_dir + "direction"

with open(led_mode, "wb") as f:
  f.write("out")

with open(led_pin, "wb") as f:
  f.write(__import__("sys").argv[1])

"""
Contributors!

Danilo J. S. Bellini
Estevão U. P. Vieira
Lucas  S. Simões
Thiago M. Sanches
Paulo R. O. Castro

AEEEW!!!! =D
"""
