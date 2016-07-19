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
  <DigitalPin GPIO:17 @ Local:11>
  >>>
  >>> led_pin = board.pins[11]
  >>> led_pin.set_mode(pingo.OUT)
  >>> led_pin.on()
  >>> led_pin.state
  1
  >>> sleep(1)  # 1 second
  >>> led_pin.off()
  >>> led_pin.state
  0
  >>> board.cleanup()

Builds the correct GPIO Device
------------------------------

::

  >>> import pingo
  >>> board2 = pingo.rpi.RaspberryPi()
  >>> pin = board2.pins[11]
  >>> board2._render_path(pin, 'direction')
  '/sys/class/gpio/gpio17/direction'
  >>> board2._render_path(pin, 'value')
  '/sys/class/gpio/gpio17/value'

