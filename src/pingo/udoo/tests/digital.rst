=============
Basic usage
=============

Turn on a led for 1s
--------------------

::

	>>> import pingo
	>>> from time import sleep
	>>>
	>>> board = pingo.udoo.Udoo()
	>>> board.pins[13]
	<DigitalPin 40>
	>>>
	>>> led_pin = board.pins[13]
	>>> led_pin.set_mode(pingo.OUTPUT)
	>>> led_pin.high()
	>>> led_pin.state
	1
	>>> sleep(1)  # 1 second
	>>> led_pin.low()
	>>> led_pin.state
	0
