import mraa
import pyupm_servo
import time

# Button on port 8 and servo on port 5
# button turns servo 0 - 90 degrees

button = mraa.Gpio(8)
button.dir(mraa.DIR_IN)

servo = pyupm_servo.ES08A(8)

flag = 0

while 1:
  if (button.read()==1):
   flag = not(flag)
   if flag:
    # Servo at 0 deg
	servo.setAngle(0)
   else:
    # Servo at 90 deg
    servo.setAngle(90)
  time.sleep(0.5)

