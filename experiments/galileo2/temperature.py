import pyupm_grove
import time

temperature = pyupm_grove.GroveTemp(0)

while 1:
  print(temperature.value())
  time.sleep(1)  