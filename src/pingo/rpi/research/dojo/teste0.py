#!/usr/bin/env python
# coding: utf-8

"""
Testes básicos com RPi.GPIO
"""

import sys
import atexit
import time

try:
    import RPi.GPIO as GPIO
except:
    print '*** Erro ao importar RPi.GPIO. Tente executar o script assim:'
    print '\tsudo python %s' % sys.argv[0]
    sys.exit(1)

# assegurar que a função cleanup será chamada na saída do script
atexit.register(GPIO.cleanup)

# usar numeração física do conector (pino 1 == 3v3)
GPIO.setmode(GPIO.BOARD)

def ver(argv):
    print 'Revisão da placa Raspberry Pi:', GPIO.RPI_REVISION
    print 'Versão da biblioteca RPi.GPIO:', GPIO.VERSION

def piscar(argv):
    try:
        pino = int(argv[2])
    except (IndexError, ValueError):
        print 'modo de usar:'
        print '\tsudo python piscar NUMERO_DO_PINO'
        sys.exit(1)
    GPIO.setup(pino, GPIO.OUT)
    print 'ligando pino', pino
    GPIO.output(pino, 1)
    time.sleep(1)
    print 'desligando pino', pino
    GPIO.output(pino, 0)

if __name__=='__main__':
    if len(sys.argv) >= 2:
       comando = sys.argv[1]
       try:
           globals()[comando](sys.argv)
       except KeyError:
           print 'comando desconhecido:', comando


