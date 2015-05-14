SPECIAL_CMD = b'\x7C'
MOVE_CMD = b'\xFE'


class LCD16x2(object):

    def __init__(self, port, baudrate=9600):
        import serial as py_serial
        self.uart = py_serial.Serial(port, baudrate)

    def clear(self):
        self.uart.write(SPECIAL_CMD + b'\x01')

    def set_cursor(self, line=0, column=0):
        first_pos = (128, 192)
        code = first_pos[line] + column
        self.uart.write(MOVE_CMD + chr(code))

    def write(self, octets):
        self.uart.write(octets)

    def __repr__(self):
        cls_name = self.__class__.__name__
        return '<{} at {!r}>'.format(cls_name, self.uart.port)
