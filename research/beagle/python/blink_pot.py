import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

from time import sleep

# pinos = [16, 21, 22, 13, 12, 11]

GPIO.setup("P9_16", GPIO.OUT)

while True:
    GPIO.output("P9_16", GPIO.HIGH)
    sleep(1)
    GPIO.output("P9_16", GPIO.LOW)
    #sleep(1)

