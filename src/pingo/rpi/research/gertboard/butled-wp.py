#!/usr/bin/env python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard butled test 
# by Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, 
# but check it yourself.
import wiringpi
import sys
board_type = sys.argv[-1]

wiringpi.wiringPiSetupGpio()                # initialise wiringpi
wiringpi.pinMode(22, 0)                     # set up ports for input
wiringpi.pinMode(24, 0)
wiringpi.pullUpDnControl(23, wiringpi.PUD_UP)   # set port 23 pull-up 

def reset_ports():                      # resets the ports for a safe exit
    wiringpi.pinMode(22,0)              # set ports to input mode
    wiringpi.pinMode(24,0)
    wiringpi.pullUpDnControl(23, wiringpi.PUD_OFF) #unset pullup

if board_type == "m":
    print "These are the connections you must make on the Multiface for this test:"
    print "GPIO 23 --- 3 in BUFFERS"
    print "GPIO 22 --- 6 in BUFFERS"
    print "BUFFER DIRECTION SETTINGS 3, pin 2 --- 6 in top header (next to leds)"
    print "jumper on BUFFER DIRECTION SETTINGS 'IN' 6"

else:
    print "These are the connections you must make on the Gertboard for this test:"
    print "GP23 in J2 --- B3 in J3"
    print "GP22 in J2 --- B6 in J3"
    print "U3-out-B3 pin 1 --- BUF6 in top header"
    print "jumper on U4-in-B6"
raw_input("When ready hit enter.\n")

button_press = 0                          # set intial values for variables
previous_status = ''

try:
    while button_press < 20:  # read inputs constantly until 19 changes are made
        status_list = [wiringpi.digitalRead(23), wiringpi.digitalRead(22)]
        for i in range(0,2):
            if status_list[i]:
                status_list[i] = "1"
            else:
                status_list[i] = "0" 
                        # dump current status values in a variable
        current_status = ''.join((status_list[0],status_list[1]))
                        # if that variable not same as last time
        if current_status != previous_status:
            print current_status                # print the results                         
                        # update status variable for next comparison
            previous_status = current_status
                        # increment button_press counter
            button_press += 1

except KeyboardInterrupt:               # trap a CTRL+C keyboard interrupt
    reset_ports()                       # resets GPIO ports
reset_ports()           # on finishing,reset all GPIO ports used by this program
