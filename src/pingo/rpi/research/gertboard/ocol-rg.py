#!/usr/bin/env python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard ocol test by 
# Gert Jan van Loo & Myra VanInwegen. Use at your own risk
# I'm pretty sure the code is harmless, but check it yourself.

import RPi.GPIO as GPIO
from time import sleep
import sys
board_type = sys.argv[-1]
if board_type == "m":
    poss_channels = 7
else:
    poss_channels = 6

def which_channel():
    print "Which driver do you want to test?"
    # User inputs channel number
    channel = raw_input("Type a number between 1 and %d\n" % poss_channels) 
    # Check valid user input
    while not channel.isdigit():
        # Make them do it again if wrong                                  
        channel = raw_input("Try again - just numbers 1-%d please!\n" % poss_channels)
    return channel

channel = 0           # set channel to 0 initially so it will ask for user input

# ask for a channel until answer between 1 & 6/7 given
while not 0 < channel < (poss_channels + 1):
    channel = int(which_channel())          # once proper answer given, carry on

# Print On-screen Instructions
print "These are the connections for the open collector test:"
if board_type == "m":
    print "GPIO 4 --- %d in RLY DRIVERS" % channel
    print "+ of external power source --- PWR in J6"
    print "ground of external power source --- GND (any)"
    print "ground side of your circuit --- %d in J12" % (channel)
    print "+ of your circuit --- PWR (any)"
else:
    print "GP4 in J2 --- RLY%d in J4" % channel
    print "+ of external power source --- RPWR in J6"
    print "ground of external power source --- GND (any)"
    print "ground side of your circuit --- RLY%d in J%d" % (channel, channel+11)
    print "+ of your circuit --- RPWR (any)"
raw_input("When ready hit enter.\n")

GPIO.setmode(GPIO.BCM)                              # initialise RPi.GPIO
GPIO.setup(4, GPIO.OUT)                             # set up port 4 for output

try:
    for i in range(10):                             # do this 10 times
        GPIO.output(4, 1)                           # switch port 4 on
        sleep(0.4)                                  # wait 0.4 seconds
        GPIO.output(4, 0)                           # switch port 4 off
        sleep(0.4)

except KeyboardInterrupt:                  # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                         # resets all GPIO ports

GPIO.cleanup()          # on finishing,reset all GPIO ports used by this program
