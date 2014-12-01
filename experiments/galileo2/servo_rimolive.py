import pingo

import mraa

import time

class Servo(object):

    MAX_PERIOD = 7968
    MAX_ANGLE = 180.0
    current_angle = 0
    
    def __init__(self, pin, min_pulse=600, max_pulse=2500):
        pin.mode = pingo.OUT
	self.pin = pin
	self.min_pulse = min_pulse
	self.max_pulse = max_pulse

    def setAngle(self, angle):
        period = (self.max_pulse - self.min_pulse) / self.MAX_ANGLE
        
	cycles = int(100.0 * (abs(self.current_angle - angle) / self.MAX_ANGLE))
	servo = mraa.Pwm(self.pin.location)
	for cycle in range(0,cycles):
            servo.period_us(self.MAX_PERIOD)
            servo.pulsewidth_us(self.calculatePulse(angle))
        self.current_angle = angle
        print 'pulse = ', self.calculatePulse(angle), ', cycles = ', cycles

    def calculatePulse(self, value):
        if value > self.MAX_ANGLE:
            return self.max_pulse
        if value < 0:
            return self.min_pulse
        return int(float(self.min_pulse) + (float((value / self.MAX_ANGLE)) * (float(self.max_pulse) - float(self.min_pulse))))


if __name__ == '__main__':
    board = pingo.detect.MyBoard()
    pin = board.pins[3]
    servo = Servo(pin)
    #servo.setAngle(90)
    while True:
        servo.setAngle(0)
        time.sleep(1)
        servo.setAngle(90)
        time.sleep(1)