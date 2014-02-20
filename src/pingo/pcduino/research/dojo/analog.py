#!/usr/bin/env python

"""
Analog:
ler valor de um pino de entrada analogico
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

import time

ADC_PATH = '/proc/'

def analog(pin):
    with open(ADC_PATH+'adc%s'%pin, 'r') as f:
        f.seek(0)
        return f.read()

while True:
    lido = analog(5)
    num = int(lido.split(':')[1])
    v = num*3.3/4096
    barra = int(v/3.3 * 40) * '='
    t = time.time()
    #time.sleep(.2)
    print '%.2f %-14r %4d %0.2f %s' % (t, lido, num, v, barra)
