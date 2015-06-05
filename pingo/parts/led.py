import pingo

import time
import threading


class Led(object):
    """A single LED"""

    def __init__(self, pin, lit_state=pingo.HIGH):
        """Set lit_state to pingo.LOW to turn on led by bringing
           cathode to low state.

        :param lit_state: use pingo.HI for anode control, pingo.LOW
                          for cathode control
        """

        pin.mode = pingo.OUT
        self.pin = pin
        self.lit_state = lit_state
        self.blink_task = None

    def on(self):
        if self.lit_state == pingo.HIGH:
            self.pin.high()
        else:
            self.pin.low()

    def off(self):
        if self.lit_state == pingo.HIGH:
            self.pin.low()
        else:
            self.pin.high()

    @property
    def lit(self):
        return self.pin.state == self.lit_state

    @property
    def blinking(self):
        return self.blink_task is not None and self.blink_task.active

    def toggle(self):
        self.pin.toggle()

    def blink(self, times=3, on_delay=.5, off_delay=None):
        """
        :param times: number of times to blink (0=forever)
        :param on_delay: delay while LED is on
        :param off_delay: delay while LED is off
        """
        if self.blinking:
            self.stop()
        self.blink_task = BlinkTask(self, times, on_delay, off_delay)
        threading.Thread(target=self.blink_task.run).start()

    def stop(self):
        """Stop blinking"""
        if self.blinking:
            self.blink_task.terminate()
            self.blink_task = None

PURE_COLORS = [
    ('RED',    [1, 0, 0]),
    ('YELLOW', [1, 1, 0]),
    ('GREEN',  [0, 1, 0]),
    ('CYAN',   [0, 1, 1]),
    ('BLUE',   [0, 0, 1]),
    ('PURPLE', [1, 0, 1]),
]


class RGBLed(object):

    def __init__(self, red_pin, green_pin, blue_pin,
                 lit_state=pingo.LOW):
        self._leds = [Led(red_pin, lit_state), Led(green_pin, lit_state),
                      Led(blue_pin, lit_state)]
        for led in self._leds:
            led.off()

    def cycle(self, delay=.2):
        for led in self._leds:
            led.on()
            time.sleep(delay)
            led.off()


class BlinkTask(object):

    def __init__(self, led, times, on_delay, off_delay):
        """
        :param led: Led instance to to blink
        :param times: number of times to blink (0=forever)
        :param on_delay: delay while LED is on
        :param off_delay: delay while LED is off
        """
        self.led = led
        self.active = True
        self.forever = times == 0
        self.times_remaining = times
        self.on_delay = on_delay
        self.off_delay = off_delay if off_delay is not None else on_delay
        self.led.off()

    def terminate(self):
        self.active = False

    def run(self):
        while self.active and (self.forever or self.times_remaining):
            self.led.toggle()
            if self.led.lit:
                time.sleep(self.on_delay)
                if not self.forever:
                    self.times_remaining -= 1
            else:
                time.sleep(self.off_delay)
        else:
            self.led.off()
            self.active = False


DIGIT_MAP = {
    0: '1111110',
    1: '0110000',
    2: '1101101',
    3: '1111001',
    4: '0110011',
    5: '1011011',
    6: '1011111',
    7: '1110000',
    8: '1111111',
    9: '1111011',
    10: '1110111',
    11: '0011111',
    12: '1001110',
    13: '0111101',
    14: '1001111',
    15: '1000111',
    'G': '1011110',  # to spell GArOA
    'r': '0000101',  # to spell GArOA
}


class SevenSegments(object):

    def __init__(self, pin_a, pin_b, pin_c, pin_d,
                 pin_e, pin_f, pin_g, pin_dp=None,
                 lit_state=pingo.HIGH):
        self._leds = [Led(pin_a, lit_state), Led(pin_b, lit_state),
                      Led(pin_c, lit_state), Led(pin_d, lit_state),
                      Led(pin_e, lit_state), Led(pin_f, lit_state),
                      Led(pin_g, lit_state)]

        if pin_dp:
            self._leds.append(Led(pin_dp, lit_state))

        self._digit = 0
        self._dot = False

    def _configure(self, pattern):
        for segment, state in zip(self._leds, pattern):
            if state == '1':
                segment.on()
            else:
                segment.off()

    @property
    def digit(self):
        return self._digit

    @digit.setter
    def digit(self, digit):
        self._digit = digit
        pattern = DIGIT_MAP[digit]
        self._configure(pattern)

    def on(self):
        self.digit = self._digit

    def off(self):
        self._configure('0' * 7)

    @property
    def dot(self):
        return self._dot

    @dot.setter
    def dot(self, state):
        if len(self._leds) < 8:
            raise LookupError('Decimal point LED undefined')
        if state:
            self._dot = True
            self._leds[7].on()
        else:
            self._dot = False
            self._leds[7].off()
