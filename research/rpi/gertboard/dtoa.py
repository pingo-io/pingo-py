#!/usr/bin/python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard dtoa test by Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, but check it yourself.
# This will not work unless you have installed py-spidev as in the README.txt file
# spi must also be enabled on your system

import spidev
import sys
from time import sleep
board_type = sys.argv[-1]

# reload spi drivers to prevent spi failures
import subprocess
unload_spi = subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi = subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)
sleep(3)

def which_channel():
    channel = raw_input("Which channel do you want to test? Type 0 or 1.\n")  # User inputs channel number
    while not channel.isdigit():                                              # Check valid user input
        channel = raw_input("Try again - just numbers 0 or 1 please!\n")      # Make them do it again if wrong
    return channel

spi = spidev.SpiDev()
spi.open(0,1)        # The Gertboard DAC is on SPI channel 1 (CE1 - aka GPIO7)

channel = 3                         # set initial value to force user selection
common = [0,0,0,160,240]            # 2nd byte common to both channels
voltages = [0.0,0.5,1.02,1.36,2.04] # voltages for display
                                                
while not (channel == 1 or channel == 0):       # channel is set by user input
    channel = int(which_channel())              # continue asking until answer 0 or 1 given
if channel == 1:                                # once proper answer given, carry on
    num_list = [176,180,184,186,191]            # set correct channel-dependent list for byte 1
else:
    num_list = [48,52,56,58,63]

print "These are the connections for the digital to analogue test:"

if board_type == "m":
    print "jumper connecting GPIO 7 to CSB"
    print "Multimeter connections (set your meter to read V DC):"
    print "  connect black probe to GND"
    print "  connect red probe to DA%d on D/A header" % channel

else:
    print "jumper connecting GP11 to SCLK"
    print "jumper connecting GP10 to MOSI"
    print "jumper connecting GP9 to MISO"
    print "jumper connecting GP7 to CSnB"
    print "Multimeter connections (set your meter to read V DC):"
    print "  connect black probe to GND"
    print "  connect red probe to DA%d on J29" % channel

raw_input("When ready hit enter.\n")

for i in range(5):
    r = spi.xfer2([num_list[i],common[i]])                   #write the two bytes to the DAC
    print "Your meter should read about %.2fV" % voltages[i]   
    raw_input("When ready hit enter.\n")

r = spi.xfer2([16,0])  # switch off channel A = 00010000 00000000 [16,0]
r = spi.xfer2([144,0]) # switch off channel B = 10010000 00000000 [144,0]

# The DAC is controlled by writing 2 bytes (16 bits) to it. 
# So we need to write a 16 bit word to DAC
# bit 15 = channel, bit 14 = ignored, bit 13 =gain, bit 12 = shutdown, bits 11-4 data, bits 3-0 ignored
# You feed spidev a decimal number and it converts it to 8 bit binary
# each argument is a byte (8 bits), so we need two arguments, which together make 16 bits.
# that's what spidev sends to the DAC. If you need to delve further, have a look at the datasheet. :)

