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
    GhostBoard: <DigitalPin @13> mode -> OUT
    >>> led_pin.on()
    GhostBoard: <DigitalPin @13> state -> HIGH
    >>> led_pin.state
    'HIGH'
    >>> sleep(1)  # 1 second
    >>> led_pin.off()
    GhostBoard: <DigitalPin @13> state -> LOW
    >>> led_pin.state
    'LOW'
    >>> led_pin.toggle()
    GhostBoard: <DigitalPin @13> state -> HIGH
    >>> led_pin.toggle()
    GhostBoard: <DigitalPin @13> state -> LOW
    >>> board.cleanup()
    GhostBoard: cleaning up.
