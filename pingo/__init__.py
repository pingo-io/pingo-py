# api
from board import ANALOG, IN, OUT, PWM, HIGH, LOW
from board import ModeNotSuported, WrongPinMode
from board import PwmOutputCapable, AnalogInputCapable, Board
from board import PwmPin, AnalogPin, DigitalPin, GroundPin, Pin, VccPin
import parts

# boards
import rpi
import ghost
import udoo
import pcduino
import arduino
import bbb

# resources
import detect
import test
