#!/usr/bin/python2.7
# Python 2.7 version by Alex Eames of http://RasPi.TV 
# functionally equivalent to the Gertboard potmot test by 
# Gert Jan van Loo & Myra VanInwegen
# Use at your own risk - I'm pretty sure the code is harmless, but you are
# responsible for checking  it yourself.
# This will not work unless you have installed py-spidev and wiringpi for Python
# as described in the README.txt file. SPI must also be enabled on your system

# This is a simplified combination of the atod.py and motor-wp.py programs.
# The potentiometer position (read by the ADC) determines 
# motor direction and speed (PWM value)
# Middle value = no movement. 1023 = Max one way, 0 = Max the other way.

from __future__ import print_function       
from time import sleep

# reload spi drivers to prevent spi failures
import subprocess
unload_spi = subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi = subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)
sleep(3)

import spidev                         
import wiringpi
import sys
board_type = sys.argv[-1]

wiringpi.wiringPiSetupGpio()                # Initialise wiringpi GPIO
wiringpi.pinMode(18,2)                      # Set up GPIO 18 to PWM mode
wiringpi.pinMode(17,1)                      # GPIO 17 to output
wiringpi.digitalWrite(17, 0)                # port 17 off for rotation one way
wiringpi.pwmWrite(18,0)                     # set pwm to zero initially

def get_adc(channel):                     # read SPI data from MCP3002 chip
    if ((channel > 1) or (channel < 0)):  # Only channels 0 and 1 else return -1
        return -1
    r = spi.xfer2([1,(2+channel)<<6,0])   # these two lines explained at end
    ret = ((r[1]&31) << 6) + (r[2] >> 2)
    return ret 

def reset_ports():                          # resets the ports for a safe exit
    wiringpi.pwmWrite(18,0)                 # set pwm to zero
    wiringpi.digitalWrite(18, 0)            # ports 17 & 18 off
    wiringpi.digitalWrite(17, 0)
    wiringpi.pinMode(17,0)                  # set ports back to input mode
    wiringpi.pinMode(18,0)

channel = iterations = 0                    # set ADC channel to 0 

print ("These are the connections for the potentiometer - motor test:")

if board_type == "m":
    print ("jumper connecting GPIO 8 to CSA")
    print ("Potentiometer connections:")
    print ("  (call 1 and 3 the ends of the resistor and 2 the wiper)")
    print ("  connect 3 to 3V3")
    print ("  connect 2 to AD%d" % channel);
    print ("  connect 1 to GND")
    print ("Motor connections:")
    print ("GPIO 17 --- MOTB")
    print ("GPIO 18 --- MOTA")
    print ("+ of external power source --- MOTOR +")
    print ("ground of external power source --- MOTOR - ")
    print ("one wire for your motor in MOTOR A screw terminal")
    print ("the other wire for your motor in MOTOR B screw terminal")

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
    print ("Motor connections:")
    print ("GP17 in J2 --- MOTB (just above GP1)")
    print ("GP18 in J2 --- MOTA (just above GP4)")
    print ("+ of external power source --- MOT+ in J19")
    print ("ground of external power source --- GND (any)")
    print ("one wire for your motor in MOTA in J19")
    print ("the other wire for your motor in MOTB in J19")

raw_input("When ready hit enter.\n")

spi = spidev.SpiDev()
spi.open(0,0)         # The Gertboard ADC is on SPI channel 0 (CE0 - aka GPIO8)

try:
    while iterations < 600:
        adc_value = (get_adc(channel))  # read ADC voltage to control motor

        if adc_value > 511:                 # above half-way on the pot
            wiringpi.digitalWrite(17, 0)    # motor spins one way
            pwm = (adc_value - 511) * 2 -1
        else:                               # below half-way on the pot
            wiringpi.digitalWrite(17, 1)    # motor spins the other way
            pwm = adc_value * 2 + 1

        wiringpi.pwmWrite(18, pwm)          # send PWM value to port 18

        sleep(0.05)        # need a delay 
        iterations += 1    # limit duration of program run to 30s [600 * 0.05]

except KeyboardInterrupt:                   # trap a CTRL+C keyboard interrupt
    reset_ports()                           # reset ports on interrupt 

reset_ports()       # reset ports on normal exit

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
# spi.xfer2 returns same number of 8-bit bytes as sent. In this case, three 
# 8-bit bytes are returned. We must then parse out the correct 10-bit byte 
# from the 24 bits returned. The above line discards all bits but the 10 data
# bits from the center of the last 2 bytes: XXXX XXXX - XXXX DDDD - DDDD DDXX 
