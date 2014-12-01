import pyupm_grove as grove
import time

led = grove.GroveLed(2)
for x in range(0, 5):
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)
