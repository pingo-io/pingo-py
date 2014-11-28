Pingo means "pin, go!"
======================

.. image:: https://secure.travis-ci.org/garoa/pingo.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/garoa/pingo

.. image:: https://coveralls.io/repos/garoa/pingo/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/garoa/pingo

Pingo provides a uniform API to program devices like the Raspberry Pi, BeagleBone Black, pcDuino etc. just like the Python DBAPI provides an uniform API for database programming in Python.

The API is object-oriented but easy to use: a board is an instance of a ``Board`` subclass. Every board has a dictionary called ``pins`` which lists all GPIO pins on the board. Each pin is an instance of a ``Pin`` subclass with attributes that you can inspect to learn about its capabilities.

The name `Pingo`_ is a tribute to `Garoa Hacker Clube`_, where the project started (the words *pingo* and *garoa* are related in Portuguese). To our English-speaking friends we like to say that it means **"pin, go!"** -- the main purpose of this package.

.. _Pingo: https://garoa.net.br/wiki/Pingo
.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Garoa_Hacker_Clube:About


.. _basic-usage:

-----------
Basic usage
-----------

To use ``pingo``, the first step is to instatiate a concrete `Board`. Each Pingo driver is a concrete board, for example, ``pingo.rpi.RaspberryPi`` and ``pingo.arduino.ArduinoFirmata`` are two such boards.

Pingo can automatically detect the board in most common cases. If it is running on a supported board, ``pingo.detect.MyBoard()`` returns an proper board instance. If Pingo is running on an unsupported machine (eg. a PC running GNU/Linux), it will try to find a remote Arduino using the Firmata protocol via USB and -- if succesfull -- will return a ``pingo.arduino.ArduinoFirmata`` instance.

Once you have a board instance, its possible to access its pins through the ``board.pins`` dict.

.. code-block:: python

    import pingo
    from time import sleep

    board = pingo.detect.MyBoard()
    led_pin = board.pins[13]
    led_pin.mode = pingo.OUT

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

===================== ======== =============== ======== ==================================================
Board                 Type     Module/Package  Status   Notes
===================== ======== =============== ======== ==================================================
Arduino Firmata       remote   arduino         level 1  requires `firmata protocol`_ on any Arduino board
Arduino Yún           on-board                 experim. requires `Bridge sketch`_ on the Arduino Yún
TI BeagleBone Black   on-board bbb             experim.
Cubietech Cubieboard  on-board                 none
Fantasma              fake     ghost           level 1  not a real board, just a software fake for testing
SolidRun HummingBoard on-board                 none
Intel Galileo         on-board galileo         none
TI MSP430             remote                   none     requires `firmata protocol`_ on any MSP430 board
LinkSprite pcDuino    on-board pcduino         level 1
element14 RaspberryPi on-board rpi             level 0  requires `RPi.GPIO`_ on the Raspberry Pi
SECO UDOO             on-board udoo            level 0
===================== ======== =============== ======== ==================================================

.. _Firmata protocol: http://arduino.cc/en/reference/firmata
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
