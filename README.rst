pingo
=====

Generic API for controlling boards with programmable IO pins

Basic usage
-----------

Code to turn on a led for 1s on an Raspberry Pi::

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

To do the same on a Arduino Yún, just change the line were the board is instantiated, and the pin numbers as needed::

	>>> board = pingo.ard.ArduinoYun()
	>>> board.pins[13]
	<DigitalPin #13>
	>>>
	>>> led_pin = board.pins[13]
	>>> led_pin.mode = pingo.OUTPUT
	>>> led_pin.state = 1
	>>> led_pin.state
	1
	>>> sleep(1)  # 1 second
	>>> led_pin.state = 0
	>>> led_pin.state
