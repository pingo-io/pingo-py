import serial
import time

SPECIAL_CMD = b'\x7C'
MOVE_CMD = b'\xFE'

class LCD16x2(object):
    
    def __init__(self, port, baudrate=9600):
        self.serial = serial.Serial(port, baudrate)
        
    def clear(self):
        self.serial.write(SPECIAL_CMD + b'\x01')
    
    def set_cursor(self, line=0, column=0):
        first_pos = (128, 192)
        code = first_pos[line] + column
        self.serial.write(MOVE_CMD + chr(code))
        
    def write(self, octets):
        self.serial.write(octets)
        
