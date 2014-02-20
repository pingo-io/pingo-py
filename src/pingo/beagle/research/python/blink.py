import atexit
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

from time import sleep

def sair():
    print 'encerrando...'
    GPIO.cleanup()

atexit.register(sair)

GPIO.setup("P9_16", GPIO.OUT)

while True:
    GPIO.output("P9_16", GPIO.HIGH)
    sleep(1)
    GPIO.output("P9_16", GPIO.LOW)
    sleep(1)

