#!/usr/bin/python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard dad test by Gert Jan van Loo 
# & Myra VanInwegen. Use at your own risk - I'm pretty sure the code is
# harmless, but check it yourself.
# This will not work unless you have installed py-spidev (see README.txt file)
# spi must also be enabled on your system
import spidev
import sys

# reload spi drivers to prevent spi failures
import subprocess
from time import sleep
unload_spi = subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi = subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)

board_type = sys.argv[-1]
print board_type

def dac_write(DAC_value):                                   # this functions as an SPI driver for the DAC
    spi.open(0,1)                                           # Gertboard DAC is on SPI channel 1 (CE1 - aka GPIO7)
    bin_data_bits = int(bin(DAC_value)[2:])                     # it converts your number 0-255 into two binary
    bin_data_bits = "{0:08d}".format(bin_data_bits)             # bytes and writes them to the SPI port via spidev
    whole_list = [dac_channel,0,gain,1,bin_data_bits,'0000']    # assemble whole 16 bit string in a list
    final_bitstring = ''.join( map( str, whole_list ) )         # join it all in one 16 bit binary string
    byte1 = int(final_bitstring[0:8],2)                         # split into two 8 bit bytes
    byte2 = int(final_bitstring[8:16],2)                        # and convert to denary for spidev
    r = spi.xfer2([byte1,byte2])                                # send spidev the two denary numbers

def get_adc(channel):                                   # read SPI data from MCP3002 chip
    spi.open(0,0)                                       # Gertboard ADC is on SPI channel 0 (CE0 - aka GPIO8)
    if ((channel > 1) or (channel < 0)):                # Only 2 channels 0 and 1 else return -1
        return -1
    r = spi.xfer2([1,(2+channel)<<6,0])     # these two lines are an spi driver for the ADC, they send three bytes
    ret = ((r[1]&31) << 6) + (r[2] >> 2)    # and receive back three. This line extracts the 0-1023 ADC reading
    return ret 
                                # set some variables. We can set more than one on a line if values the same
dac_channel = gain = 1          # dac_channel is channel B on the dac (not SPI channel) gain is the DAC gain
adc_channel = DAC_value = 0     # refers to channel A on the adc, also set intial DAC_value = 0
char='#'                        # set the bar chart character
spi = spidev.SpiDev()           # spidev is the python 'wrapper' enabling us to 'speak' to the SPI port

print("These are the connections for the digital to analogue to digital test:")

if board_type == "m":
    print("jumper connecting GPIO 8 to CSA")
    print("jumper connecting GPIO 7 to CSB")
    print("jumper connecting DA1 to AD0 on the A/D D/A header")

else:
    print("jumper connecting GP11 to SCLK")
    print("jumper connecting GP10 to MOSI")
    print("jumper connecting GP9 to MISO")
    print("jumper connecting GP8 to CSnA")
    print("jumper connecting GP7 to CSnB")
    print("jumper connecting DA1 on J29 to AD0 on J28")


sleep(3)
raw_input("When ready hit enter.\n")

print "dig ana"
for DAC_value in range(0,257,32):   # go from 0-256 in steps of 32 (note the loop stops at 256 not 257)
    if DAC_value==256:
        DAC_value=255               # DAC can only accept 0-255, but that's not divisible by 32, so we 'cheat' 
    dac_write(DAC_value)
    adc_value = get_adc(adc_channel)
    adc_string = "{0:04d}".format(adc_value)            # read ADC and make output a 4 character string
    print "%s %s %s" % ("{0:03d}".format(DAC_value), adc_string, (adc_value)/16 * char)

for DAC_value in range(224,-1,-32):
    dac_write(DAC_value)
    adc_value = get_adc(adc_channel)
    adc_string = "{0:04d}".format(adc_value)            # read ADC and make output a 4 character string
    print "%s %s %s" % ("{0:03d}".format(DAC_value), adc_string, (adc_value)/16 * char)

r = spi.xfer2([144,0]) # switch off DAC channel 1 (B) = 10010000 00000000 [144,0]
