#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import time
import RPi.GPIO as GPIO

# assegurar que a função cleanup será chamada na saída do script
atexit.register(GPIO.cleanup)

# usar numeração lógica dos pinos
GPIO.setmode(GPIO.BCM)

PORTAS = [17, 4, 9, 11, 7, 27, 22, 10]

for porta in PORTAS:
    GPIO.setup(porta, GPIO.OUT)
    GPIO.output(porta, 1)
    time.sleep(.5)
