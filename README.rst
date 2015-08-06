Pingo means "pin, go!"
======================

.. image:: https://secure.travis-ci.org/pingo-io/pingo-py.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/pingo-io/pingo-py

.. image:: https://coveralls.io/repos/pingo-io/pingo-py/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/pingo-io/pingo-py

Pingo provides a uniform API to program devices like the Raspberry Pi, BeagleBone Black, pcDuino etc. just like the Python DBAPI provides an uniform API for database programming in Python.

The API is object-oriented but easy to use: a board is an instance of a ``Board`` subclass. Every board has a dictionary called ``pins`` which lists all GPIO pins on the board. Each pin is an instance of a ``Pin`` subclass with attributes that you can inspect to learn about its capabilities.

The name `Pingo`_ is a tribute to `Garoa Hacker Clube`_, where the project started (the words *pingo* and *garoa* are related in Portuguese). To our English-speaking friends we like to say that it means **"pin, go!"** -- the main purpose of this package.

.. _Pingo: https://garoa.net.br/wiki/Pingo
.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Garoa_Hacker_Clube:About

-----
Media
-----

Watch it on Youtube: https://www.youtube.com/watch?v=pAOooxPL_tQ

.. image:: https://img.youtube.com/vi/pAOooxPL_tQ/maxresdefault.jpg
    :alt: Intel IoT RoadShow São Paulo 2014
    :target: https://www.youtube.com/watch?v=pAOooxPL_tQ
    :align: center

Intel IoT RoadShow São Paulo 2014

.. _basic-usage:

-----------
Basic usage
-----------

To use ``pingo``, the first step is to instantiate a ``Board``. Each Pingo driver is a concrete board subclass, for example, ``pingo.rpi.RaspberryPi`` and ``pingo.arduino.ArduinoFirmata`` are two such classes.

Pingo can automatically detect the board in most common cases. If the script is running on a supported board, ``pingo.detect.get_board()`` returns an suitable board instance. If Pingo is running on an unsupported machine (eg. a notebook), it will try to find a connected Arduino using the Firmata protocol via USB and -- if successful -- will return a ``pingo.arduino.ArduinoFirmata`` instance.

Once you have a board instance, it's possible to access its pins through the ``board.pins`` dictionary:

.. code-block:: python

    import pingo
    from time import sleep

    board = pingo.detect.get_board()
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

``pingo.pcduini.PcDuino`` ``pingo.galileo.Galileo2`` are examples of drivers, and the respective ``PcDuino`` and ``Galileo2`` are subclasses of the ``pingo.board.Board`` abstract class that defines the common API for all boards.

The following table lists the drivers currently planned or under development.

===================== ======== =================== ======== ==================================================
Board                 Type     Module/Package      Status   Notes
===================== ======== =================== ======== ==================================================
Arduino Firmata       remote   ``arduino.firmata`` level 2  requires `firmata protocol`_ on any Arduino board
Arduino Yún           on-board ``arduino.yun``     level 2  requires `Bridge sketch`_ on the Arduino Yún
BeagleBone Black      on-board ``bbb``             experim.
Intel Galileo Gen 2   on-board ``intel.galileo``   level 2  requires Intel IoT Dev Kit `mraa`_ library
Intel Edison          on-board ``intel.edison``    level 2  requires Intel IoT Dev Kit `mraa`_ library
LinkSprite pcDuino    on-board ``pcduino``         level 1
RaspberryPi           on-board ``rpi``             level 0  requires `RPi.GPIO`_ on the Raspberry Pi
SECO UDOO             on-board ``udoo``            level 0
===================== ======== =================== ======== ==================================================

.. _Firmata protocol: http://arduino.cc/en/reference/firmata
.. _Bridge sketch: http://arduino.cc/en/Reference/YunBridgeLibrary
.. _RPi.GPIO: https://pypi.python.org/pypi/RPi.GPIO
.. _mraa: https://github.com/intel-iot-devkit/mraa

We are also interested in supporting: Banana Pi, Cubietech Cubieboard, SolidRun HummingBoard, TI MSP430 (via `firmata protocol`_ ).

In a addition, Pingo implements ``ghost``, a mock software-only board for testing the API.


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
    Nothing has been done yet. Great opportunity for you to contribute with experiments and/or start a new driver.
