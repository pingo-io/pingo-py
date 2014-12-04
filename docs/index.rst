Introduction
============

Pingo provides a uniform API to program devices like the Raspberry Pi, pcDuino, Intel Galileo etc. just like the Python DBAPI provides an uniform API for database programming in Python.

The API is object-oriented but easy to use: each board is an instance of a ``Board`` subclass. Every board has a dictionary called ``pins`` which lists all GPIO pins on the board. Each pin is an instance of a ``Pin`` subclass with attributes that you can inspect to learn about its capabilities.

A single script can easily control more than board at the same time. For example, a program running on the pcDuino can control the pcDuino itself and two Arduinos connected to the pcDuino via USB using the Firmata protocol. 

The name `Pingo`_ is a tribute to `Garoa Hacker Clube`_, where the project started (in Portuguese, "pingo" is drop and "garoa" is drizzle). To our English-speaking friends we like to say **Pingo means: "pin, go!"** -- this nicely sums up the purpose of this package.

.. _Pingo: https://garoa.net.br/wiki/Pingo
.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Garoa_Hacker_Clube:About

.. _basic-usage:

.. include:: ../README.rst
    :start-after: _basic-usage:

------------
Installation
------------

There are two ways of installing Pingo:

1. from Python PyPI
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


-------------------
More documentation
-------------------

Contents:

.. toctree::
   :maxdepth: 2

   API
   contributing

Indices and tables
--------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


