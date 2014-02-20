#!/usr/bin/env python
# coding: utf-8

from pyun import *

yun = YunBridge('192.168.2.9')

pinos = [6, 7, 8, 13, 11, 10]

for p in pinos:
    yun.pinMode(p, OUTPUT)

while True:
    for p in pinos:
        yun.digitalWrite(p, 1)
        pot = yun.analogRead(0)
        print p, pot
        yun.delay(pot)
        yun.digitalWrite(p, 0)
