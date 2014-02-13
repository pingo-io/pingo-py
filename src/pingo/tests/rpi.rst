=============
Basic usage
=============

Turn on a led for 1s
--------------------

::

	>>> from time import sleep
	>>> import pingo
	>>>
	>>> board = pingo.rpi.RaspberryPi()
	>>> board.pins[11]
	<DigitalPin #11>
	>>>
	>>> led_pin = board.pins[11]
	>>> led_pin.mode = pingo.OUTPUT
	>>> led_pin.state = 1
	>>> led_pin.state
	1
	>>> sleep(1)  # 1 second
	>>> led_pin.state = 0
	>>> led_pin.state
	0
