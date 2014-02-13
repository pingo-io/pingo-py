from board import Board

class RaspberryPi(Board):

    def __init__(self):
        self.pins = {11:DigitalPin(11)}

class Pin(object):

    def __init__(self, physical_pin):
        self.physical_pin = physical_pin

    def __repr__(self):
        return '<%s #%d>' % (
            self.__class__.__name__,
            self.physical_pin)

class GroundPin(Pin):
    pass

class VddPin(Pin):
    pass

class DigitalPin(Pin):
    pass

