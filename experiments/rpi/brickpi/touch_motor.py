# Luciano Ramalho
# This code is for testing the BrickPi with a Lego Touch Sensor and a Motor
# 
# Adapted from code by Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/

"""touch_motor.py

1) connect a Lego motor to port "MA" of the BrickPi
2) connect a Lego touch sensor to port "S1" of the BrickPi
3) push/release the sensor to turn the motor on/low
"""

print __doc__.strip()

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_TOUCH   #Set the type of sensor at PORT_1

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    if not result :
        touch_state = BrickPi.Sensor[PORT_1]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
    #LR: is this needed? this is from LEGO-Touch_Sensor_Test.py 
    time.sleep(.01)     # sleep for 10 ms
    if touch_state:
        BrickPi.MotorSpeed[PORT_A] = 255  #Set the speed of MotorA (-255 to 255)
    else:
    	BrickPi.MotorSpeed[PORT_A] = 0
