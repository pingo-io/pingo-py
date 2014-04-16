#!/usr/bin/python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard atod test by 
# Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, 
# but check it yourself.
# This will not work unless you have installed py-spidev (see README.txt)
# spi must also be enabled on your system (also in README.txt)

# import Python 3 print function to prevent line breaks. All prints need ()
from __future__ import print_function       
from time import sleep

# reload spi drivers to prevent spi failures
import subprocess
unload_spi = subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi = subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)
sleep(3)

import spidev
import sys
board_type = sys.argv[-1]                        

def which_channel():
    channel = raw_input("Which channel do you want to test? Type 0 or 1.\n")  # User inputs channel number
    while not channel.isdigit():                                              # Check valid user input
        channel = raw_input("Try again - just numbers 0 or 1 please!\n")      # Make them do it again if wrong
    return channel

def get_adc(channel):                                   # read SPI data from MCP3002 chip
    if ((channel > 1) or (channel < 0)):                # Only 2 channels 0 and 1 else return -1
        return -1
    r = spi.xfer2([1,(2+channel)<<6,0])  # these two lines are explained in more detail at the bottom
    ret = ((r[1]&31) << 6) + (r[2] >> 2)
    return ret 

def display(char, reps, adc_value, spaces):        # function handles the display of ##### 
    print ('\r',"{0:04d}".format(adc_value), ' ', char * reps, ' ' * spaces,'\r', sep='', end='') 
    sys.stdout.flush()

iterations = 0             # initial value for iteration counter
char = '#'                 # define the bar chart character
channel = 3                # set channel to 3 initially so it will ask for user input (must be 0 or 1)

while not (channel == 1 or channel == 0):       # continue asking until answer 0 or 1 given
    channel = int(which_channel())              # once proper answer given, carry on

print ("These are the connections for the analogue to digital test:")

if board_type == "m":
    print ("jumper connecting GPIO 8 to CSA")

else:
    print ("jumper connecting GP11 to SCLK")
    print ("jumper connecting GP10 to MOSI")
    print ("jumper connecting GP9 to MISO")
    print ("jumper connecting GP8 to CSnA")

print ("Potentiometer connections:")
print ("  (call 1 and 3 the ends of the resistor and 2 the wiper)")
print ("  connect 3 to 3V3")
print ("  connect 2 to AD%d" % channel);
print ("  connect 1 to GND")

raw_input("When ready hit enter.\n")

spi = spidev.SpiDev()
spi.open(0,0)          # The Gertboard ADC is on SPI channel 0 (CE0 - aka GPIO8)

while iterations < 600:
    adc_value = (get_adc(channel))
    reps = adc_value / 16
    spaces = 64 - reps
    display(char, reps, adc_value, spaces)
    sleep(0.05)       # need a delay so people using ssh don't get slow response
    iterations += 1   # limits length of program running to 30s [600 * 0.05]

# SPI communication based on a code snippet anonymously posted here...
# http://proxy.obd2tool.com/index.php?url=1n151A1t1r1r1D1z0I1CyX1s0UyGyFyMyb1v121t1lyd0Kyj1tyN1xya 

# EXPLANATION of 
# r = spi.xfer2([1,(2+channel)<<6,0])
# Send start bit, sgl/diff, odd/sign, MSBF 
# channel = 0 sends 0000 0001 1000 0000 0000 0000
# channel = 1 sends 0000 0001 1100 0000 0000 0000
# sgl/diff = 1; odd/sign = channel; MSBF = 0 

# EXPLANATION of 
# ret = ((r[1]&31) << 6) + (r[2] >> 2)
# spi.xfer2 returns same number of 8-bit bytes as sent. In this case, three 8-bit bytes are returned
# We must then parse out the correct 10-bit byte from the 24 bits returned. The following line discards
# all bits but the 10 data bits from the center of the last 2 bytes: XXXX XXXX - XXXX DDDD - DDDD DDXX 
