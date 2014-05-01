# coding: utf-8

import atexit

from abc import ABCMeta, abstractmethod


HIGH = 'HIGH'
LOW = 'LOW'
IN = 'IN'
OUT = 'OUT'


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

    Implementations of ``Board`` subclasses should:

    * Call ``super(«BoardSubclass», self).__init__()`` and
      ``self.add_pins(«pins»)`` in their ``__init__`` method.

    * Implement ``_set_pin_mode()`` and ``_set_pin_state()``.

    * Override ``cleanup()``, if the board needs it.

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

        The ``«pin».mode(…)`` property calls this method because
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
    """Defines common interface for all digital pins.

    Implementers of board drivers do not need to subclass this class
    because pins delegate all board-dependent behavior to the board.
    """

    def __init__(self, board, location, gpio_id=None):

        Pin.__init__(self, board, location, gpio_id)
        self._mode = None
        self._state = None

    @property
    def mode(self):
        """[property] Get/set pin mode to ``pingo.IN`` or ``pingo.OUT``"""
        return self._mode

    @mode.setter
    def mode(self, value):
        self.board._set_pin_mode(self, value)
        self._mode = value

    @property
    def state(self):
        """[property] Get/set pin state to ``pingo.HIGH`` or ``pingo.LOW``"""
        if self.mode == IN:
            self._state = self.board._get_pin_state(self)

        return self._state

    @state.setter
    def state(self, value):
        if self.mode != OUT:
            raise WrongPinMode()

        self.board._set_pin_state(self, value)
        self._state = value

    def low(self):
        """Set voltage of pin to ``pingo.LOW`` (GND)."""
        self.state = LOW

    lo = low  # shortcut for interactive use

    def high(self):
        """Set state of the pin to ``pingo.HIGH`` (Vcc)."""
        self.state = HIGH

    hi = high  # shortcut for interactive use

    def toggle(self):
        self.state = HIGH if self.state == LOW else LOW


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
