#!/usr/bin/env python

from ctypes import CDLL
# LIB_ARDUINO = '/home/ubuntu/sample/core/libarduino.so'
LIB_ARDUINO = './ard2.so'
print 'testes', LIB_ARDUINO

lib = CDLL(LIB_ARDUINO)
print lib
