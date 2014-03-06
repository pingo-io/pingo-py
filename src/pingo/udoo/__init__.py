from pingo.board import Board, DigitalPin

# there are no gaps in the Arduino digital pin numbering of the 
# Due and the Udoo
# pin_list[arduino_pin] -> gpio_pin

pin_list = [
    116, 112, 20, 16, 17, 18, 41, 42, 21, 19, 1, 9, 3, 40, 150, 
    162, 160, 161, 158, 159, 92, 85, 123, 124, 125, 126, 127, 133, 
    134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 54, 205, 32, 
    35, 34, 33, 101, 144, 145, 89, 105, 104, 57, 56, 55, 88
]

class Udoo(Board):

    def __init__(self):
        self.add_pins((physical, DigitalPin(logical)) for physical, logical in enumerate(pin_list))
        self.pin_path_mask = '/sys/class/gpio/gpio%d/'
        
