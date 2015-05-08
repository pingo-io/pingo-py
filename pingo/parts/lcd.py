

class Lcd(object):
    """A LCD Display"""

    def __init__(self, rst_pin, en_pin, d0_pin, d1_pin, d2_pin, d3_pin):
        """
        :param rst_pin: The reset pin for LCD
        :param en_pin: The enable pin for LCD
        :param d0_pin: The D0 pin for LCD
        :param d1_pin: The D1 pin for LCD
        :param d2_pin: The D2 pin for LCD
        :param d3_pin: The D3 pin for LCD
        """
        rst_pin.mode = pingo.OUT
        en_pin.mode = pingo.OUT
        d0_pin.mode = pingo.OUT
        d1_pin.mode = pingo.OUT
        d2_pin.mode = pingo.OUT
        d3_pin.mode = pingo.OUT
        self.rst = rst_pin
        self.en = en_pin
        self.data = [d0_pin, d1_pin, d2_pin, d3_pin]


    def printString(self, value, col = None, row = None):
        self.rst.hi()
        write(value >> 4)
        write(value)


    def write(self, value):
       for i in range(0,4):
            data[i].state = (value >> i> & 0x01
