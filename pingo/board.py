import atexit

HIGH = 'HIGH'
LOW = 'LOW'
INPUT = 'IN'
OUTPUT = 'OUT'

class DisabledPin(StandardError):
    value = 'Use pin.set_mode(mode) before using a pin.'

class WrongPinMode(StandardError):
    value = 'Operation not supported in current mode.'


class Board(object):

    def __init__(self):
        """ register self.cleanup for calling at script exit
        """
        if hasattr(self, 'cleanup'):
            atexit.register(self.cleanup)

    def add_pins(self, pins):
        """ pins is an iterable of Pin instances
        """
        self.pins = {}
        for pin in pins:
            self.pins[pin.location] = pin

    def _set_pin_mode(self, pin, mode):
        raise NotImplementedError

    def _set_pin_state(self, pin, state):
        raise NotImplementedError


class Pin(object):

    def __init__(self, board, location, gpio_id=None):
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

    def __init__(self, board, location, gpio_id=None):
        Pin.__init__(self, board, location, gpio_id)
        self.enabled = False
        self.mode = INPUT

    def set_mode(self, mode):
        self.board._set_pin_mode(self, mode)
        self.mode = mode
        self.enabled = True

    def _change_state(self, state):
        if not self.enabled:
            raise DisabledPin()

        if self.mode != OUTPUT:
            raise WrongPinMode()

        self.board._set_pin_state(self, state)
        self.state = state

    def low(self):
        self._change_state(LOW)

    def high(self):
        self._change_state(HIGH)


class GroundPin(Pin):

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

class VddPin(Pin):

    def __init__(self, board, location, voltage):
        Pin.__init__(self, board, location)
        self.voltage = voltage  # e.g. 3.3, 5.0

    def __repr__(self):
        return '<%s %0.1fV>' % (
                self.__class__.__name__,
                self.voltage)
