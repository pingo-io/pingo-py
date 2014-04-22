=============
Basic usage
=============

Turn on a led for 1s
--------------------

::

    >>> import pingo
    >>> sleep = lambda x: None
    >>>
    >>> board = pingo.ghost.GhostBoard()
    >>> board.pins[13]
    <DigitalPin @13>
    >>>
    >>> led_pin = board.pins[13]
    >>> led_pin.mode = pingo.OUT
    >>> led_pin.on()
    >>> led_pin.state
    'HIGH'
    >>> sleep(1)  # 1 second
    >>> led_pin.off()
    >>> led_pin.state
    'LOW'
    >>> board.cleanup()
    GhostBoard: cleaning up.
