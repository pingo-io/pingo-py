
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1

class Board(object):

    def add_pins(self, pins):
        """ pins is an iterable of Pin instances
        """
        self.pins = {}
        for pin in pins:
            self.pins[pin.location] = pin

    def set_pin_mode(self, pin, mode):
        raise NotImplementedError

class Pin(object):

    def __init__(self, board, location, gpio_id=None):
        self.board = board
        self.location = location
        self.gpio_id = gpio_id

    def __repr__(self):
        return '<%s %s@%r>' % (
                self.__class__.__name__,
                '' if self.gpio_id is None else repr(self.gpio_id),
                self.location)

class DigitalPin(Pin):

    def __init__(self, board, location, gpio_id=None, mode=INPUT, state=LOW):
        Pin.__init__(self, board, location, gpio_id)
        self.set_mode(mode)
        self.state = state

    def set_mode(self, mode):
        self.board.set_pin_mode(self, mode)
        self.mode = mode

    def low(self):
        self.board.set_pin_state(self, LOW)
        self.state = LOW

    def high(self):
        self.board.set_pin_state(self, HIGH)
        self.state = HIGH


class GroundPin(Pin):

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

class VddPin(Pin):
    def __init__(self, board, voltage):
        Pin.__init__(self, board)
        self.voltage = voltage

    def __repr__(self):
        return '<%s %s>' % (
                self.__class__.__name__,
                self.voltage)




INPUT = 0
OUTPUT = 1

