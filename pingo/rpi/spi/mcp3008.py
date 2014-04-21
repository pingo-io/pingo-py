#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Object interface for MCP3008 A/D converter using bit-banged SPI
"""

__author__ = 'Luciano Ramalho'

import time
import os
import atexit
import RPi.GPIO as GPIO

# make sure GPIO.cleanup will be called when script exits
atexit.register(GPIO.cleanup)

class Mcp3008(object):
    def __init__(self, spi_clock, spi_miso, spi_mosi, spi_cs):
        self.clock = spi_clock
        self.miso = spi_miso
        self.mosi = spi_mosi
        self.cs = spi_cs
        GPIO.setmode(GPIO.BCM)
        for port in [self.clock, self.mosi, self.cs]:
            GPIO.setup(port, GPIO.OUT)
        GPIO.setup(self.miso, GPIO.IN)

    def read(self, channel):
        assert 0 <= channel <= 7, 'channel must be 0...7'
        GPIO.output(self.cs, True)    
        GPIO.output(self.clock, False)
        GPIO.output(self.cs, False)
        cmd = channel
        cmd |= 0x18  # start bit + "single-ended" config bit
        cmd <<= 3    # discard 3 bits; we need just 5
        for i in range(5):
            GPIO.output(self.mosi, cmd & 0x80)
            cmd <<= 1
            GPIO.output(self.clock, True)
            GPIO.output(self.clock, False)

        res = 0
        # read null bit plus 10 bits for ADC value
        for i in range(11):
            GPIO.output(self.clock, True)
            GPIO.output(self.clock, False)
            res <<= 1
            if (GPIO.input(self.miso)):
                res |= 0x1

        GPIO.output(self.cs, True)
        return res

def test():
    # select pins for SPI
    SPI_CLK = 18
    SPI_MISO = 23
    SPI_MOSI = 24
    SPI_CS = 25
    ad_chip = Mcp3008(SPI_CLK, SPI_MISO, SPI_MOSI, SPI_CS)
    count = 0
    display = '{0:6d}  {1:010b}  {1:4}  {2:3.2f} V {3}'
    while True:
        res = ad_chip.read(1)
        volts = float(res)/1023 * 3.3
        ticks = int(round(float(res)/1023*40))*'='
        print display.format(count, res, volts, ticks)
        time.sleep(.2)
        count += 1
    
if __name__=='__main__':
    test()
