
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1

class Board(object):

    def add_pins(self, pin_map):
        """ pin_map is a list of pairs: [(pin_location, pin_instance), ...]
            where pin_location is a physical pin id and pin_instance is
            an instance of Pin
        """
        self.pins = {}
        for pin_location, pin in pin_map:
            if pin is not None:
                pin.board = self
                self.pins[pin_location] = pin

    def set_pin_mode(self, pin, mode):
        raise NotImplementedError

class Pin(object):

    def __init__(self, board, location, logical_id=None):
        self.board = board
        self.location = location
        self.logical_id = logical_id

    def __repr__(self):
        return '<%s %s@%r>' % (
                self.__class__.__name__,
                '' if self.logical_id is None else repr(self.logical_id),
                self.location)

class DigitalPin(Pin):

    def __init__(self, board, logical_id, mode=OUTPUT, state=LOW):
        Pin.__init__(self, board, logical_id)
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

