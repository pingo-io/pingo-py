#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import time
import RPi.GPIO as GPIO
import pingo

# call cleanup at program exit
atexit.register(GPIO.cleanup)

# use BCM logic numbering
GPIO.setmode(GPIO.BCM)

DISPLAY = [17, 4, 9, 11, 7, 27, 22, 10]

SPI_CLK = 18  # @12 (physical pin)
SPI_MISO = 23  # @16
SPI_MOSI = 24  # @18
SPI_CS = 25  # @22
ad_converter = pingo.spi.Mcp3008(SPI_CLK, SPI_MISO, SPI_MOSI, SPI_CS)

POT_CHANNEL = 1

for led in DISPLAY[:6]:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

while True:
    for led in DISPLAY[:6]:
        GPIO.output(led, 1)
        delay = ad_converter.read(POT_CHANNEL) / 1000.0
        time.sleep(delay)
        GPIO.output(led, 0)
