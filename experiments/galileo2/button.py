import mraa
from time import sleep

button = mraa.Gpio(6)
button.dir(mraa.DIR_IN)

while(button.read()!=1):
    print 'Press button to quit'
    sleep(0.3)

print 'The End'
