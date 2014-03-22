#!/usr/bin/env python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard buttons test by 
# Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, 
# but check it yourself.

import RPi.GPIO as GPIO
import sys
board_type = sys.argv[-1]

GPIO.setmode(GPIO.BCM)                  # initialise RPi.GPIO
for i in range(23,26):                  # set up ports 23-25 
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # as inputs pull-ups high      

# Print  Instructions appropriate for the selected board
if board_type == "m":
    print "These are the connections for the Multiface buttons test:" 
    print "GPIO 25 --- 1 in BUFFERS"
    print "GPIO 24 --- 2 in BUFFERS"
    print "GPIO 23 --- 3 in BUFFERS"
    print "Optionally, if you want the LEDs to reflect button state do the following:"
    print "jumper on BUFFER DIRECTION SETTINGS, OUT 1"
    print "jumper on BUFFER DIRECTION SETTINGS, OUT 2"
    print "jumper on BUFFER DIRECTION SETTINGS, OUT 3"

else:
    print "These are the connections for the Gertboard buttons test:"
    print "GP25 in J2 --- B1 in J3"
    print "GP24 in J2 --- B2 in J3"
    print "GP23 in J2 --- B3 in J3"
    print "Optionally, if you want the LEDs to reflect button state do the following:"
    print "jumper on U3-out-B1"
    print "jumper on U3-out-B2"
    print "jumper on U3-out-B3"

raw_input("When ready hit enter.\n")

button_press = 0        # set intial values for variables
previous_status = ''

try:
    while button_press < 20:             # read inputs until 19 changes are made
        status_list = [GPIO.input(25), GPIO.input(24), GPIO.input(23)]
        for i in range(0,3):
            if status_list[i]:
                status_list[i] = "1"
            else:
                status_list[i] = "0"
        # dump current status values in a variable
        current_status = ''.join((status_list[0],status_list[1],status_list[2]))
        # if that variable not same as last time 
        if current_status != previous_status:
            print current_status                # print the results 
            # update status variable for next comparison
            previous_status = current_status
            button_press += 1                   # increment button_press counter

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program
GPIO.cleanup()                     # on exit, reset all GPIO ports 
