import pyupm_grove
import time

pot = pyupm_grove.GroveRotary(0)

while 1:
  print(pot.abs_deg())
  time.sleep(0.5)
