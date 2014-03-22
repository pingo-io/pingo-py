import Adafruit_BBIO.ADC as ADC

from time import sleep

ADC.setup()

pino = 'P9_36'
    
while True:
    v1 = ADC.read(pino)
    sleep(.01)
    v2 = ADC.read(pino)
    print '%s %10.3f |%20s| %10.3f |%20s|' % (
            pino, v1, int(v1*20) * '#', v2, int(v2*20) * '#'),
    print # '*' * int(tempo*60)
    sleep(.01)
