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


DIGIT_MAP = (0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70,
             0x7F, 0x7B, 0x77, 0x1F, 0x4E, 0x3D, 0x4F, 0x47)


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
