#!/usr/bin/env python
# coding: utf-8
# MIT Licenced
# @authors: Danilo J. S. Bellini
#           Eduardo F. Mendes
#           Renato G. Rodrigues
#           Victor Mendizabal
#           Otto Heringer
#           Danilo Vieira
#
# Regular time-alternated one-LED blinking with AudioLazy for Raspberry Pi

import RPi.GPIO as gpio
from time import sleep
from audiolazy import Stream

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)

for idx, delay in enumerate(Stream(1, 2, 2, 1)):
    gpio.output(11, int(idx % 2 == 0))
    sleep(delay * .2)

