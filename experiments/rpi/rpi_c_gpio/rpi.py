import ctypes
import atexit

HIGH = 'HIGH'
LOW = 'LOW'
IN = 'IN'
OUT = 'OUT'


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
        self.mode = IN

    def set_mode(self, mode):
        self.board._set_pin_mode(self, mode)
        self.mode = mode

    def _change_state(self, state):
        if self.mode != OUT:
            raise WrongPinMode()

        self.board._set_pin_state(self, state)
        self.state = state

    def low(self):
        self._change_state(LOW)

    def high(self):
        self._change_state(HIGH)

    def get(self):
        if self.mode != IN:
            raise WrongPinMode()

        return self.board._get_pin_state(self)


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
# connector_p1_location: gpio_id
DIGITAL_PIN_MAP = {
    3: 2,
    5: 3,
    7: 4,
    8: 14,
    10: 15,
    11: 17,
    12: 18,
    13: 27,
    15: 22,
    16: 23,
    18: 24,
    19: 10,
    21: 9,
    22: 25,
    23: 11,
    24: 8,
    26: 7,
}

class cRaspberryPi(Board):

    def __init__(self):
        super(cRaspberryPi, self).__init__()
        self.dll = ctypes.cdll.LoadLibrary("./fsgpio.so");

        pins = [VccPin(self, 1, 3.3),
                VccPin(self, 2, 5.0),
                VccPin(self, 4, 5.0),
                VccPin(self, 17, 3.3)]

        pins += [GroundPin(self, n) for n in [6, 9, 14, 20, 25]]

        pins += [DigitalPin(self, location, gpio_id)
                 for location, gpio_id in DIGITAL_PIN_MAP.items()]

        self.add_pins(pins)

    def cleanup(self):
        for pin in self.pins.values():
            if hasattr(pin, 'enabled') and pin.enabled:
                self.dll.disable_pin(int(pin.gpio_id));
                pin.enabled = False

    def _set_pin_mode(self, pin, mode):
        if hasattr(pin, 'enabled') and not pin.enabled:
            self.dll.enable_pin(int(pin.gpio_id));
            pin.enabled = True
        _mode = 'out' if mode == OUT else 'in'
        self.dll.set_pin_direction(int(pin.gpio_id), mode)

    def _set_pin_state(self, pin, state):
        _state = '1' if state == HIGH else '0'
        self.dll.set_pin_value(int(pin.gpio_id), _state)

    def _get_pin_state(self, pin):
        return self.dll.get_pin_value(4)

