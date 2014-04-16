#!/usr/bin/env python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard buttons test 
# by Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, 
# but check it yourself.

import wiringpi
import sys
board_type = sys.argv[-1]

wiringpi.wiringPiSetupGpio()                        # initialise wiringpi
for port_num in range(23,26):
    wiringpi.pinMode(port_num, 0)                   # set up ports for input
    wiringpi.pullUpDnControl(port_num, wiringpi.PUD_UP) #set pullups

def reset_ports():                          # resets the ports for a safe exit
    for i in range(23,26):
        wiringpi.pinMode(i,0)               # set ports to input mode
        wiringpi.pullUpDnControl(i, wiringpi.PUD_OFF) #unset pullups

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
button_press = 0                            # set intial values for variables
previous_status = ''

try:
    while button_press < 20:    # read inputs constantly until 19 changes made
        status_list = [wiringpi.digitalRead(25), wiringpi.digitalRead(24), wiringpi.digitalRead(23)]
        for i in range(0,3):
            if status_list[i]:
                status_list[i] = "1"
            else:
                status_list[i] = "0"
                                # dump current status values in a variable
        current_status = ''.join((status_list[0],status_list[1],status_list[2]))
                                # if that variable not same as last time
        if current_status != previous_status:               
            print current_status                 # print the results
                                # update status variable for next comparison
            previous_status = current_status
                                # increment button_press counter
            button_press += 1

except KeyboardInterrupt:                 # trap a CTRL+C keyboard interrupt
    reset_ports()                         # resets GPIO ports
reset_ports()           # on finishing,reset all GPIO ports used by this program
