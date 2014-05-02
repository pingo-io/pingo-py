Introduction
============

Pingo provides a uniform API to program devices like the Raspberry Pi, BeagleBone Black, pcDuino etc. just like the Python DBAPI provides an uniform API for database programming in Python.

The API is object-oriented but easy to use: a board is an instance of a ``Board`` subclass. Every board has a dictionary called ``pins`` which lists all GPIO pins on the board. Each pin is an instance of a ``Pin`` subclass with attributes that you can inspect to learn about its capabilities.

The name `Pingo`_ is a tribute to `Garoa Hacker Clube`_, where the project started (the words *pingo* and *garoa* are related in Portuguese). To our English-speaking friends we like to say that it means **"pin, go!"** -- the main purpose of this package.

.. _Pingo: https://garoa.net.br/wiki/Pingo
.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Garoa_Hacker_Clube:About

------------
Installation
------------

Basicly, there are two ways of installing Pingo:

1. from Python Pip
2. from Github (recommended)

Installing from PyPI
--------------------------

To install Pingo from PyPI (Python Package Index), first, make sure you have ``pip`` installed in your machine. On Linux machines, this usually means you have the `python-pip` package installed. You can check if you have ``pip`` in your machine by typing the following text on a shell prompt::

    $ pip --version
    pip 1.5.4 from /usr/lib/python2.7/dist-packages (python 2.7) 
 
If the output is similar from the one above, you can install Pingo by simple typing ``pip install pingo`` as root on you terminal. That's it!


Installing from Github
----------------------------

Since Pingo is currently in alpha state and under heavy develpment, installing Pingo from Github may be a good idea. Besides that, it will be easy for you to contribute to the project, if you wish. See the Contributing section on the left menu.

To install Pingo from Github, you must have Git installed. Presuming you already have that, just type::

    $ git clone https://github.com/garoa/pingo.git

After that, get into the pingo directory and setup Python to use your brand new directory as a library::

    $ python setup.py develop

Done! You are ready to program using Pingo!


-----------
Basic usage
-----------

``blink.py`` on an UDOO board:

.. code-block:: python

    import pingo
    from time import sleep

    board = pingo.udoo.Udoo()
    led_pin = board.pins[13]
    led_pin.set_mode(pingo.OUT)

    while True:
        led_pin.on()
        sleep(1)
        led_pin.off()
        sleep(1)

To do the same on a Arduino Yún, just change the line where the board is instantiated, and the pin numbers as needed:

.. code-block:: python

    import pingo
    from time import sleep

    board = pingo.arduino.yun.YunBridge()  # <---
    led_pin = board.pins[13]
    led_pin.set_mode(pingo.OUT)

    while True:
        led_pin.on()
        sleep(1)
        led_pin.off()
        sleep(1)


In the examples above, ``pingo.udoo`` ``pingo.arduino.yun`` are drivers, and the respective ``Udoo`` and ``YunBridge`` are classes implementing the ``pingo.board.Board`` interface.

.. _drivers-table:

.. include:: ../README.rst
    :start-after: _drivers-table:
