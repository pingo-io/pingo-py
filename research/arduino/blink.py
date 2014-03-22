#!/usr/bin/env python
# coding: utf-8

from pyun import *

yun = YunBridge('192.168.2.9')
yun.pinMode(13, OUTPUT)

while True:
    yun.digitalWrite(13, 1)
    yun.delay(1000)
    yun.digitalWrite(13, 0)
    yun.delay(1000)
