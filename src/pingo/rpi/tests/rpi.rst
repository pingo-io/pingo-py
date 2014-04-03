=============
Basic usage
=============

Turn on a led for 1s
--------------------

::

	>>> # from time import sleep
	>>> sleep = lambda x: None
	>>> import pingo
	>>>
	>>> board = pingo.rpi.RaspberryPi()
	>>> board.pins[11]
	<DigitalPin #11>
	>>>
	>>> led_pin = board.pins[11]
	>>> led_pin.set_mode(pingo.OUTPUT)
	>>> led_pin.high()
	>>> led_pin.state
	1
	>>> sleep(1)  # 1 second
	>>> led_pin.low()
	>>> led_pin.state
	0

Builds the correct GPIO Device
--------------------

::

    >>> import pingo
    >>> board = pingo.rpi.RaspberryPi()
    >>> pin = board.pins[11]
    >>> board._render_path(pin, direction)
    /sys/class/gpio/gpio11/direction
    >>> board._render_path(pin, value)
    /sys/class/gpio/gpio11/value
	
