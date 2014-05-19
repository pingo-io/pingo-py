pingo
=====

Pingo provides a uniform API to program devices like the Raspberry Pi, BeagleBone Black, pcDuino etc. just like the Python DBAPI provides an uniform API for database programming in Python.

The API is object-oriented but easy to use: a board is an instance of a ``Board`` subclass. Every board has a dictionary called ``pins`` which lists all GPIO pins on the board. Each pin is an instance of a ``Pin`` subclass with attributes that you can inspect to learn about its capabilities.

The name `Pingo`_ is a tribute to `Garoa Hacker Clube`_, where the project started (the words *pingo* and *garoa* are related in Portuguese). To our English-speaking friends we like to say that it means **"pin, go!"** -- the main purpose of this package.

.. _Pingo: https://garoa.net.br/wiki/Pingo
.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Garoa_Hacker_Clube:About

-----------
Basic usage
-----------

In order to run `Pingo`_ you need a Board instantiated, so you can get a Pin instance.
Each Board's hardware pins are manipulated via a Pin instance.
For example, in a Arduino: it is needed an instance of pingo.arduino.ArduinoFirmata
You can also use the detect.MyBoard function to get the right driver for your board.
With a board instance, its possible to access pins thru Board.pins dict.

.. code-block:: python

    import pingo
    from time import sleep

    board = pingo.detect.MyBoard()
    led_pin = board.pins[13]
    led_pin.mode pingo.OUT

    while True:
        led_pin.hi()
        sleep(1)
        led_pin.lo()
        sleep(1)

.. _drivers-table:

-------
Drivers
-------

``pingo.udoo.udoo`` ``pingo.arduino.yun`` are examples of drivers, and the respective ``Udoo`` and ``YunBridge`` are extends the ``pingo.board.Board`` interface class.

The following table lists the drivers currently planned or under development.

================ ======== =============== ======== ==================================================
Board            Type     Module/Package  Status   Notes
================ ======== =============== ======== ==================================================
Arduino Firmata  remote   arduino         level 1  requires `firmata library`_ on any Arduino board
Arduino Yún      on-board arduino.yun     experim. requires `Bridge sketch`_ on the Arduino Yún
BeagleBone Black on-board bbb             experim.
Fantasma         fake     ghost           level 1  not a real board, just a software fake for testing
Intel Galileo    on-board galileo         none
Raspberry Pi     on-board rpi             level 0  requires `RPi.GPIO`_ on the Raspberry Pi
pcDuino          on-board pcduino         level 1
UDOO             on-board udoo            level 0
================ ======== =============== ======== ==================================================

.. _Firmata library: http://arduino.cc/en/reference/firmata
.. _Bridge sketch: http://arduino.cc/en/Reference/YunBridgeLibrary
.. _RPi.GPIO: https://pypi.python.org/pypi/RPi.GPIO

Types of drivers
----------------

on-board
    Pingo and user code run on the board itself, using the Python interpreter installed in it.

remote
    Pingo and user code run on host computer connected to board, controlling the board remotely. Useful for boards that are unable to run Python, like the Arduino UNO.

fake
    Pingo and user code run on host computer emulating a dummy board in software. Useful for testing base classes from ``board.py`` and for teaching and demonstration.

.. _status-of-drivers:

Status of drivers
-----------------

level 0
    Digital I/O: get/set high/low status of digital pins (no PWM support).

level 1
    Analog input: read values from analog pins.

level 2
    PWM output: set variable value for digital pins with PWM capability.

experiments
    Some Python experiments have been done with the board. See the ``experiments/`` directory for code that may be helpful to start a new driver for a board.

none
    Nothing has been done. Great opportunity for you to contribute with experiments and/or start a new driver.
