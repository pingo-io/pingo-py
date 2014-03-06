
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
			pin.board = self
			self.pins[pin_location] = pin
		
class Pin(object):

    def __init__(self, logical_pin):
        self.logical_pin = logical_pin

    def __repr__(self):
        return '<%s %r>' % (
            self.__class__.__name__,
            self.logical_pin)

class GroundPin(Pin):
    pass

class VddPin(Pin):
    pass

class DigitalPin(Pin):

    def __init__(self, logical_id, mode=OUTPUT, state=LOW):
        Pin.__init__(self, logical_id)
        self.set_mode(mode)
        self.state = state

    def set_mode(self, mode):
        self.mode = mode

    def low(self):
        self.state = LOW

    def high(self):
        self.state = HIGH




INPUT = 0
OUTPUT = 1

