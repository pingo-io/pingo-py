Contributing
============

There are several ways of contributing to the Pingo project.

-----------
Use Pingo
-----------

If you use Pingo and spread the word about it, that is already very helpful!

In the :ref:`Drivers Table <drivers-table>`, check the *Status* column: drivers with *level 0*, *level 1* and *level 2* are ready to use, with the capabilities described in :ref:`status-of-drivers`.

If you find bugs or have suggestions for improvements, please report them in the Git Hub issue tracker at:

https://github.com/pingo-io/pingo-py/issues

-------------
Get in touch
-------------

If have trouble using Pingo, or would like to make suggestions or share your discoveries, our main forum is the *pingo-io* users and developers group at:

https://groups.google.com/forum/#!forum/pingo-io

If you are in São Paulo, mini-sprints for working on Pingo happen often at `Garoa Hacker Clube`_ on Wednesday evenings starting at 19:30.

.. _Garoa Hacker Clube: https://garoa.net.br/wiki/Pingo


----------------
Write examples
----------------

If you'd like to contribute with code, the easiest way to get started is writing examples using Pingo to control any board that you may have available. Many of the `Arduino examples`_ may be adapted to use Pingo.

The steps are:

0. Create an account on `Github`_ if you don't have one.
1. Fork the `pingo-io/pingo-py repository`_ on Github.
2. Clone your fork to work on it.
3. Code your examples.
4. Commit and push your changes to your fork.
5. Use the Github Web interface to submit a pull request.
6. If approved, your changes will be merged.
7. You are now a `contributor`_ to Pingo! Celebrate!!


Clone the repository, create your examples in a board subdirectory, for example ``pingo/pcduino/examples/blink.py``.

.. _Github: https://github.com
.. _pingo-io/pingo-py repository: https://github.com/pingo-io/pingo-py
.. _Arduino examples: http://arduino.cc/en/Tutorial/HomePage
.. _contributor: https://github.com/pingo-io/pingo-py/blob/master/CONTRIBUTORS.txt


----------------------------------
Contribute to an existing driver
----------------------------------

If a driver is at :ref:`level 0<status-of-drivers>`, implementing analog input will take it to :ref:`level 1<status-of-drivers>`, an important step (*level 1* is the minimum functionality needed for the classic Coding Dojo with Arduino-or-MiniPC invented at Garoa). Then there is :ref:`level 2<status-of-drivers>` and other levels yet to be defined.

Within a driver level, we can always fix bugs or improve the performance.

Before contributing to an existing driver, please coordinate with the other contributors. Send a message to the `mailing list`_ explaining what you intend to do and wait for some feedback: somebody may be working on the same driver, or have other ideas to help you.

.. _mailing list: https://groups.google.com/forum/#!forum/pingo-io

----------------------------------
Create new drivers
----------------------------------

A growing number of boards capable of running Python is coming to market. Our goal is to have Pingo support all of them.

To create a new driver the best way to start may be to copy the module and tests of a similar board. For example, UDOO and pcDuino both use ``sysfs`` as the main means of controlling the GPIO pins. At this writing, there is no pcDuino driver but there is a :ref:`level 0<status-of-drivers>` UDOO driver, so a :ref:`level 0<status-of-drivers>` pcDuino driver can be created and tested in a few hours (by the way, analog input is much easier on pcDuino than on UDOO, so a :ref:`level 1<status-of-drivers>` driver for the pcDuino would not take much longer. See the `experiments/pcduino/dojo/`_ directory).

.. _experiments/pcduino/dojo/: https://github.com/pingo-io/pingo-py/tree/master/experiments/pcduino/dojo

The `experiments/`_ directory in the main repository has scripts in Python and other languages that show basic programming of the boards. Look in that directory for code that may help you get started, or create your own experiments there to understand how to interact with the board using Python.

.. _experiments/: https://github.com/pingo-io/pingo-py/tree/master/experiments
