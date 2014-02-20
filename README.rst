pingo
=====

Generic API for controlling boards with programmable IO pins

Basic usage
-----------

Blink.py on an Raspberry Pi
.. code-block:: python

  import pingo
  from time import sleep
  
  placa = pingo.rpi.RaspberryPi()
  pino_led = placa.pins[11]
  pino_led.set_mode(pingo.OUTPUT)
  while True:
      pino_led.high()
      sleep(1)
      pino_led.low()
      sleep(1)

To do the same on a Arduino Yún, just change the line were the board is instantiated, and the pin numbers as needed
.. code-block:: python

  import pingo
  from time import sleep
  
  placa = pingo.arduino.Yun()  # <---
  pino_led = placa.pins[13]
  pino_led.set_mode(pingo.OUTPUT)
  while True:
      pino_led.high()
      sleep(1)
      pino_led.low()
      sleep(1)
