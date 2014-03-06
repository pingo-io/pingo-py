pingo
=====

Generic API for controlling boards with programmable IO pins

-----------
Basic usage
-----------

Blink.py on an UDOO board

.. code-block:: python

	import pingo
	from time import sleep

	board = pingo.udoo.Udoo()
	led_pin = board.pins[13]
	led_pin.set_mode(pingo.OUTPUT)

	while True:
		led_pin.high()
		sleep(1)
		led_pin.low()
		sleep(1)

To do the same on a Arduino Yún, just change the line were the board is instantiated, and the pin numbers as needed

.. code-block:: python

	import pingo
	from time import sleep

	board = pingo.arduino.yun.YunBridge()  # <---
	led_pin = board.pins[13]
	led_pin.set_mode(pingo.OUTPUT)

	while True:
		led_pin.high()
		sleep(1)
		led_pin.low()
		sleep(1)


-------
Drivers
-------

In the examples above, ``pingo.rpi`` ``pingo.arduino.yun`` are drivers, and the respective ``RaspberryPi`` and ``YunBridge`` are classes implementing the ``pingo.board.Board`` interface.

The following table lists the drivers currently planned or under development.

================ ======== =============== =================================================
Board            Type     Package         Notes
================ ======== =============== =================================================
Arduino Firmata  remote   arduino.firmata requires `firmata library`_ on any Arduino board
Arduino Yún      on-board arduino.yun     requires `Bridge sketch`_ on the Arduino Yún
BeagleBone Black on-board beagle
Fantasma         mock     ghost           not a real board, just a mock for testing clients
Raspberry Pi     on-board rpi
pcDuino          on-board pcduino
UDOO             on-board udoo
================ ======== =============== =================================================

.. _Firmata library: http://arduino.cc/en/reference/firmata
.. _Bridge sketch: http://arduino.cc/en/Reference/YunBridgeLibrary







