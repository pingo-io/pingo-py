# coding: utf-8

import atexit

from abc import ABCMeta, abstractmethod


HIGH = 'HIGH'
LOW = 'LOW'
IN = 'IN'
OUT = 'OUT'


class DisabledPin(Exception):
    value = 'Use pin.set_mode(mode) before using a pin.'


class WrongPinMode(Exception):
    value = 'Operation not supported in current mode.'


class Board(object):
    """Abstract class defining common interface for all boards.

    Instance attributes of interest to end-users:

    ``«board».pins``
        A ``dict`` with physical pin locations as keys and ``Pin`` instances
        as values.

    ``«board».cleanup()``
        This should be called to release the pins for other applications on
        some boards. It is called automatically when the script finishes.

    Implementers of board drivers should call ``__init__`` and ``add_pins``
    in their ``__init__`` implementations, should implement ``_set_pin_mode``
    and ``_set_pin_state`` and, if needed, override ``cleanup``.

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """Registers ``self.cleanup`` for calling at script exit.

        This ``__init__`` method should be called by the ``__init__``
        of all ``Board`` subclasses using ``super(MyBoard, self).__init__()``.
        The ``__init__`` of board subclasses should also call
        ``self.add_pins(pins)`` with an iterable of ``Pin`` instances.
        """
        atexit.register(self.cleanup)

    def add_pins(self, pins):
        """Populate ``board.pins`` mapping from ``Pin`` instances.

        Arguments:
            ``pins``: an iterable of ``Pin`` instances
        """
        self.pins = {}
        for pin in pins:
            self.pins[pin.location] = pin

    @abstractmethod
    def _set_pin_mode(self, pin, mode):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«pin».set_mode(…)`` method calls this method because
        the procedure to set pin mode changes from board to board.
        """

    @abstractmethod
    def _set_pin_state(self, pin, state):
        """Abstract method to be implemented by each ``Board`` subclass

        The ``«pin».__change_state(…)`` method calls this method because
        the procedure to set pin state changes from board to board.
        """

    def cleanup(self):
        """Releases pins for use by other applications.

        Overriding this stub may or may not be needed in specific drivers.
        For example, scripts running on boards using standard ``sysfs``
        GPIO access should ``unexport`` the pins before exiting.
        """
        pass


class Pin(object):
    """Abstract class defining common interface for all pins."""
    __metaclass__ = ABCMeta

    def __init__(self, board, location, gpio_id=None):
        """Initialize ``Pin`` instance with

        Arguments:
            ``board``
                The board to which the pin is attached.
            ``location``
                Physical location of pin; ``int`` and ``str`` are
                acceptable.
            ``gpio_id``
                Logical name of GPIO pin (e.g. ``sysfs`` file name).
        """
        self.board = board
        self.location = location
        if gpio_id is not None:
            self.gpio_id = gpio_id

    def __repr__(self):
        cls_name = self.__class__.__name__
        location = self.location
        if hasattr(self, 'gpio_id'):
            gpio_id = 'gpio%s' % self.gpio_id
        else:
            gpio_id = ''
        return '<{cls_name} {gpio_id}@{location}>'.format(**locals())


class DigitalPin(Pin):
    """Defines commmon interface to all suported pins.

    Instance attributes of interest to end-users:

    ``«pin».mode``
        The current mode of the pin: ``pingo.IN`` or ``pingo.OUT``.

    ``«pin».state``
        The current state of the pin (when in output mode):
        ``pingo.HIGH`` or ``pingo.LOW``.

    """

    def __init__(self, board, location, gpio_id=None):

        Pin.__init__(self, board, location, gpio_id)
        self.mode = IN

    def set_mode(self, mode):
        """Set pin mode to one of: ``pingo.IN`` or ``pingo.OUT``"""
        self.board._set_pin_mode(self, mode)
        self.mode = mode

    def __change_state(self, state):
        """Private method used to delegate to ``board._set_pin_state``."""
        if self.mode != OUT:
            raise WrongPinMode()

        self.board._set_pin_state(self, state)
        self.state = state

    def low(self):
        """Set voltage of pin to ``pingo.LOW`` (GND)."""
        self.__change_state(LOW)

    def high(self):
        """Set state of the pin to ``pingo.HIGH`` (Vcc)."""
        self.__change_state(HIGH)

    def get(self):
        """Get state of pin: ``pingo.HIGH`` or ``pingo.LOW``"""
        if self.mode != IN:
            raise WrongPinMode()

        return self.board._get_pin_state(self)


class GroundPin(Pin):

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


class VddPin(Pin):

    def __init__(self, board, location, voltage):
        Pin.__init__(self, board, location)
        self.voltage = voltage  # e.g. 3.3, 5.0

    def __repr__(self):
        return '<%s %0.1fV>' % (self.__class__.__name__,
                                self.voltage)
