#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import time
import RPi.GPIO as GPIO

# assegurar que a função cleanup será chamada na saída do script
atexit.register(GPIO.cleanup)

# usar numeração lógica dos pinos
GPIO.setmode(GPIO.BCM)

PINOS = [3, 5, 7, 26, 24, 21, 19, 23,  8, 10, 11, 12, 15, 16, 18, 22, 13]
BCM   = [2, 3, 4,  7,  8,  9, 10, 11, 14, 15, 17, 18, 22, 23, 24, 25, 27]
PINOS_IMPARES = [p for p in PINOS if p % 2]
PINOS_PARES = [p for p in PINOS if p % 2 == 0]

MAPA_BCM = dict(zip(PINOS, BCM))

for pino in PINOS_IMPARES[2:]:
    porta = MAPA_BCM[pino]
    print '%s,' % porta,
    GPIO.setup(porta, GPIO.OUT)
    GPIO.output(porta, 1)
    time.sleep(1)
