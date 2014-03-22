#!/usr/bin/env python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard leds test by 
# Gert Jan van Loo & Myra VanInwegen. Use at your own risk
# I'm pretty sure the code is harmless, but check it yourself.

import RPi.GPIO as GPIO
from time import sleep
import sys
board_type = sys.argv[-1]

if GPIO.RPI_REVISION == 1:      # check Pi Revision to set port 21/27 correctly
    # define ports list for Revision 1 Pi
    ports = [25, 24, 23, 22, 21, 18, 17, 11, 10, 9, 8, 7]
else:
    # define ports list all others
    ports = [25, 24, 23, 22, 27, 18, 17, 11, 10, 9, 8, 7]   
ports_rev = ports[:]                            # make a copy of ports list
ports_rev.reverse()                             # and reverse it as we need both

GPIO.setmode(GPIO.BCM)                                  # initialise RPi.GPIO

for port_num in ports:
    GPIO.setup(port_num, GPIO.OUT)                  # set up ports for output

def led_drive(reps, multiple, direction):           # define function to drive
    for i in range(reps):                      # repetitions, single or multiple
        for port_num in direction:                  # and direction
            GPIO.output(port_num, 1)                # switch on an led
            sleep(0.11)                             # wait for ~0.11 seconds
            if not multiple:                        # if we're not leaving it on
                GPIO.output(port_num, 0)            # switch it off again

# Print Wiring Instructions appropriate to the board
if board_type == "m":
    print "These are the connections for the Multiface LEDs test:"                
    print "BUFFER DIRECTION SETTINGS, jumpers on all OUT positions (1-12)"
    print "GPIO 25 --- BUFFERS 1 \nGPIO 24 --- BUFFERS 2"
    print "GPIO 23 --- BUFFERS 3 \nGPIO 22 --- BUFFERS 4"
    print "GPIO 21 --- BUFFERS 5 \nGPIO 18 --- BUFFERS 6"
    print "GPIO 17 --- BUFFERS 7 \nGPIO 11 --- BUFFERS 8"
    print "GPIO 10 --- BUFFERS 9 \nGPIO 9 --- BUFFERS 10"
    print "GPIO 8 --- BUFFERS 11 \nGPIO 7 --- BUFFERS 12"

else:
    print "These are the connections for the Gertboard LEDs test:"                
    print "jumpers in every out location (U3-out-B1, U3-out-B2, etc)"
    print "GP25 in J2 --- B1 in J3 \nGP24 in J2 --- B2 in J3"
    print "GP23 in J2 --- B3 in J3 \nGP22 in J2 --- B4 in J3"
    print "GP21 in J2 --- B5 in J3 \nGP18 in J2 --- B6 in J3"
    print "GP17 in J2 --- B7 in J3 \nGP11 in J2 --- B8 in J3"
    print "GP10 in J2 --- B9 in J3 \nGP9 in J2 --- B10 in J3"
    print "GP8 in J2 --- B11 in J3 \nGP7 in J2 --- B12 in J3"
    print "(If you don't have enough straps and jumpers you can install"
    print "just a few of them, then run again later with the next batch.)"

raw_input("When ready hit enter.\n")

try:                                        # Call the led driver function
    led_drive(3, 0, ports)                  # for each required pattern
    led_drive(1, 0, ports_rev)
        # run this once, switching off led before next one comes on, forwards
    led_drive(1, 0, ports)                  
        # run once, switch led off before next one, reverse direction
    led_drive(1, 0, ports_rev)
        # (1, 1, ports) = run once, leaving each led on, forward direction
    led_drive(1, 1, ports)
    led_drive(1, 0, ports)        
    led_drive(1, 1, ports)
    led_drive(1, 0, ports)
except KeyboardInterrupt:                   # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                          # clean up GPIO ports on CTRL+C
GPIO.cleanup()                              # clean up GPIO ports on normal exit
