import Adafruit_BBIO.ADC as ADC

from time import sleep

ADC.setup()

pino = 'P9_36'
    
while True:
    v1 = ADC.read(pino)
    sleep(.01)
    barras = int(v1*51)
    print '%s = %06.4f |%-50s|' % (pino, v1, barras * '#')
    sleep(.01)
