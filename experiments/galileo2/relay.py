import mraa
import time

# Button on port 8 and relay on port 6
# button acts as an on/off switch

button = mraa.Gpio(8)
relay = mraa.Gpio(6)

button.dir(mraa.DIR_IN)
relay.dir(mraa.DIR_OUT)

flag = 0

while 1:
  if (button.read()==1):
   flag = not(flag)
   if flag:
    relay.write(1)
    print("On")
   else:
    relay.write(0)
    print("Off")
  time.sleep(0.5)
