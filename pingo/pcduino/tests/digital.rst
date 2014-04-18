=============
Basic usage
=============

Turn on a led for 1s
--------------------

::

    >>> import pingo
    >>> from time import sleep
    >>>
    >>> board = pingo.pcduino.PcDuino()
    >>> board.pins[10]
    <DigitalPin @10>
    >>>
    >>> led_pin = board.pins[10]
    >>> led_pin.set_mode(pingo.OUT)
    >>> led_pin.high()
    >>> led_pin.state
    1
    >>> sleep(1)  # 1 second
    >>> led_pin.low()
    >>> led_pin.state
    0
