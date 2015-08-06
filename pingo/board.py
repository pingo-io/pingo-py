# coding: utf-8

import atexit
from operator import attrgetter
from abc import ABCMeta, abstractmethod

from .util import StrKeyDict

HIGH = 'HIGH'
LOW = 'LOW'

# TODO: More implementations: IN, OUT, ANALOG, PWM,
# ... IC2, SERIAL, SERVO, INTERRUPTION
IN = 'IN'
OUT = 'OUT'
ANALOG = 'ANALOG'
PWM = 'PWM'


class WrongPinMode(Exception):
    value = 'Operation not supported in current mode.'


class ModeNotSuported(Exception):
    value = 'Mode not supported by Pin or Board.'


class ArgumentOutOfRange(Exception):
    value = 'Argument not in the range 0.0 to 1.0'


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
      ``self._add_pins(«pins»)`` in their ``__init__`` method.

    * Implement ``_set_digital_mode()`` and ``_set_pin_state()``.

    * Override ``cleanup()``, if the board needs it.

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """Registers ``self.cleanup`` for calling at script exit.

        This ``__init__`` method should be called by the ``__init__``
        of all ``Board`` subclasses using ``super(BoardSubclass, self).__init__()``.
        The ``__init__`` of board subclasses should also call
        ``self._add_pins(pins)`` with an iterable of ``Pin`` instances.
        """
        atexit.register(self.cleanup)

    def filter_pins(self, *pin_types):
        """Get a list of pins that are instances of the given pin_types

        See the ``digital_pins`` property for an example of use.

        Arguments:
            ``pin_types``: an iterable of types (usually, ``Pin`` subclasses)
        """
        filtered = []
        for pin_type in pin_types:
            sub = [x for x in self.pins.values() if isinstance(x, pin_type)]
            filtered += sub

        return filtered

    def select_pins(self, locations):
        """Get list of pins from iterable of locations"""
        locations = list(locations)
        return [self.pins[location] for location in locations]

    @property
    def digital_pins(self):
        """[property] Get list of digital pins"""

        return sorted(self.filter_pins(DigitalPin), key=attrgetter('location'))

    def cleanup(self):
        """Releases pins for use by other applications.

        Overriding this stub may or may not be needed in specific drivers.
        For example, scripts running on boards using standard ``sysfs``
        GPIO access should ``unexport`` the pins before exiting.
        """
        pass

    ######################################################################
    # the following methods are of interest only to implementers of
    # drivers, i.e. concrete Board subclasses

    def _add_pins(self, pins):
        """Populate ``board.pins`` mapping from ``Pin`` instances.

        The ``__init__`` method of concrete ``Board`` subclasses should
        call this method to populate the board instance ``pins`` mapping.

        Arguments:
            ``pins``: an iterable of ``Pin`` instances
        """
        self.pins = StrKeyDict()
        self.gpio = StrKeyDict()
        for pin in pins:
            self.pins[pin.location] = pin
            if hasattr(pin, 'gpio_id'):
                self.gpio[pin.gpio_id] = pin

    @abstractmethod
    def _set_digital_mode(self, pin, mode):
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

    @abstractmethod
    def _get_pin_state(self, pin):
        """Abstract method to be implemented by each ``Board`` subclass
        """


class AnalogInputCapable(object):
    """Mixin interface for boards that support AnalogInputPin

    Concrete ``AnalogInputCapable`` subclasses should implement
    ``_get_pin_value``, and `_set_analog_mode`` to read the values
    of analog pins.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def _get_pin_value(self, pin):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«AnalogPin».value(…)`` method calls this method because
        the procedure to read pin analog signal changes from board to board.
        """

    @abstractmethod
    def _set_analog_mode(self, pin, mode):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«pin».mode(…)`` property calls this method because
        the procedure to set pin mode changes from board to board.
        """


class PwmOutputCapable(object):
    """Mixin interface for boards that support PwmOutputPin

    Concrete ``PwmOutputCapable`` subclasses should implement
    ``_get_pin_value`` to write the PWM signal of analog pins.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def _set_pwm_mode(self, pin):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«pin».mode(…)`` property calls this method because
        the procedure to set pin mode changes from board to board.
        """

    @abstractmethod
    def _set_pwm_frequency(self, pin, value):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«PwmPin».frequency(…)`` method calls this method because
        the procedure to set the PWM's frequency changes from board to board.

        This method should always be overwritten!
        If its is not possible to set PWM's frequency, a ``NotImplementedError``
        exception should be raised.
        """

    @abstractmethod
    def _set_pwm_duty_cycle(self, pin, value):
        """Abstract method to be implemented by each ``Board`` subclass.

        The ``«PwmPin».value(…)`` method calls this method because
        the procedure to set PWM's duty cycle changes from board to board.
        """

    def _get_pwm_duty_cycle(self, pin):
        """
        This method should be overwritten if the ``Board`` subclass
        has this feature.
        """
        if hasattr(pin, '_duty_cycle'):
            return pin._duty_cycle
        return 0.0

    def _get_pwm_frequency(self, pin):
        """
        This method should be overwritten if the ``Board`` subclass
        has this feature.
        """
        if hasattr(pin, '_frequency'):
            return pin._frequency
        return 0.0


class Pin(object):
    """Abstract class defining common interface for all pins.

    Attributes:
        ``supported_modes``
            Modes supported. Each ``Pin`` subclass supports different set
            of ``modes``. ``supported_modes`` is used by the ``Pin.mode``
            property. Each subclass should over overwrite this attribute.
    """
    __metaclass__ = ABCMeta

    supported_modes = []

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
        self._mode = None

    def __repr__(self):
        cls_name = self.__class__.__name__
        location = self.location
        if hasattr(self, 'gpio_id'):
            gpio_id = 'gpio%s' % self.gpio_id
        else:
            gpio_id = ''
        return '<{cls_name} {gpio_id}@{location}>'.format(**locals())

    @property
    def mode(self):
        """[property] Get/set pin mode to ``pingo.IN``, ``pingo.OUT``
         ``pingo.ANALOG`` or ``pingo.PWM``"""
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.supported_modes:
            raise ModeNotSuported()

        if value in [IN, OUT]:
            self.board._set_digital_mode(self, value)
        elif value == ANALOG:
            self.board._set_analog_mode(self, value)
        elif value == PWM:
            self.board._set_pwm_mode(self, value)

        self._mode = value


class DigitalPin(Pin):
    """Defines common interface for all digital pins.

    The ``repr`` of a digital pin looks like ``<DigitalPin gpio21@40>``
    where ``21`` is the logical pin identifier and ``40`` is the
    physical location of the pin in the connector.

    Implementers of board drivers do not need to subclass this class
    because pins delegate all board-dependent behavior to the board.
    """

    supported_modes = [IN, OUT]

    def __init__(self, board, location, gpio_id=None):
        Pin.__init__(self, board, location, gpio_id)
        self._state = None

    @property
    def state(self):
        """[property] Get/set pin state to ``pingo.HIGH`` or ``pingo.LOW``"""
        if self.mode not in [IN, OUT]:
            raise WrongPinMode()

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
        """Change state of the pin."""
        self.state = HIGH if self.state == LOW else LOW

    def pulse(self):
        """Generate a pulse in state of the pin."""
        if self.state == LOW:
            self.state = HIGH
            self.state = LOW
        else:
            self.state = LOW
            self.state = HIGH


class PwmPin(DigitalPin):

    supported_modes = [IN, OUT, PWM]

    def __init__(self, board, location, gpio_id=None, frequency=None):
        DigitalPin.__init__(self, board, location, gpio_id)
        self._frequency = frequency
        self._duty_cycle = None

    # TUDO:
    # Write a decorator to test mode == 'MODE'

    @property
    def value(self):
        if self.mode != PWM:
            raise WrongPinMode()
        return self.board._get_pwm_duty_cycle(self)

    @value.setter
    def value(self, value):
        if self.mode != PWM:
            raise WrongPinMode()
        if not 0.0 <= value <= 100.0:
            raise ArgumentOutOfRange()
        self.board._set_pwm_duty_cycle(self, value)
        self._duty_cycle = value

    @property
    def frequency(self):
        if self.mode != PWM:
            raise WrongPinMode()
        return self.board._get_pwm_frequency(self)

    @frequency.setter
    def frequency(self, new_frequency):
        if self.mode != PWM:
            raise WrongPinMode()
        if new_frequency <= 0.0:
            raise ArgumentOutOfRange()
        self.board._set_pwm_frequency(self, new_frequency)
        self._frequency = new_frequency


class AnalogPin(Pin):
    """Defines common interface for all analog pins.

    Implementers of board drivers do not need to subclass this class
    because pins delegate all board-dependent behavior to the board.

    This pin type supports read operations only.
    """

    supported_modes = [IN, ANALOG]

    def __init__(self, board, location, resolution, gpio_id=None):
        """
        :param board: the board to which this ping belongs
        :param location: the physical location of the pin on the board
        :param resolution: resolution of the AD converter in bits
        :param gpio_id: the logical id for GPIO access, if applicable
        """
        Pin.__init__(self, board, location, gpio_id)
        self.bits = resolution
        self._mode = None

    @property
    def value(self):
        """[property] Pin value as integer from 0 to 2 ** resolution - 1"""
        return self.board._get_pin_value(self)

    def ratio(self, from_min=0, from_max=None, to_min=0.0, to_max=1.0):
        """ Pin value as a float, by default from 0.0 to 1.0.

        The ``from...`` and ``to...`` parameters work like in the Arduino map_
        function, converting values from an expected input range to a desired
        output range.

        .. _map: http://arduino.cc/en/reference/map
        """
        if from_max is None:
            from_max = 2 ** self.bits - 1

        _value = self.value
        return (float(_value - from_min) * (to_max - to_min) /
                (from_max - from_min) + to_min)

    @property
    def percent(self):
        """[property] Pin value as float from 0.0 to 100.0"""
        return self.ratio(to_max=100.0)


class GroundPin(Pin):

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


class VccPin(Pin):

    def __init__(self, board, location, voltage):
        Pin.__init__(self, board, location)
        self.voltage = voltage  # e.g. 3.3, 5.0

    def __repr__(self):
        return '<%s %0.1fV>' % (self.__class__.__name__,
                                self.voltage)
