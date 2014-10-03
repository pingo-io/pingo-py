import pingo

GPIO = None

try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
else:
    class PwmWrapper(GPIO.PWM):
        def __init__(self, channel, frequency=60.):
            """
                PwmWrapper recives a integer and a float.
                - channel as GPIO number
                - PWM's frequency in Hz
            """
            self.is_running = False
            self.duty_cycle = 100.
            super(PwmWrapper, self).__init__(channel, frequency)

        def start(self, duty_cycle):
            self.is_running = True
            self.duty_cycle = duty_cycle
            return super(PwmWrapper, self).start(duty_cycle)

        def stop(self):
            self.is_running = False
            return super(PwmWrapper, self).stop()

        def ChangeDutyCycle(self, duty_cycle):
            self.duty_cycle = duty_cycle
            if not self.is_running:
                self.start(duty_cycle)
            return super(PwmWrapper, self).ChangeDutyCycle(duty_cycle)

        # TODO: ChangeFrequency


class RaspberryPi(pingo.Board, pingo.PwmOutputCapable):

    # connector_p1_location: gpio_id
    PWM_PIN_MAP = {
        3: 2,
        5: 3,
        7: 4,
        8: 14,
        10: 15,
        11: 17,
        12: 18,
        13: 27,
        15: 22,
        16: 23,
        18: 24,
        19: 10,
        21: 9,
        22: 25,
        23: 11,
        24: 8,
        26: 7,
    }

    GROUNDS_LIST = [6, 9, 14, 20, 25]

    def __init__(self):
        global GPIO
        try:
            import RPi.GPIO as GPIO
        except ImportError:
            raise ImportError('pingo.rpi.RaspberryPi requires RPi.GPIO installed')

        super(RaspberryPi, self).__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

        pins = [pingo.VccPin(self, 1, 3.3),
                pingo.VccPin(self, 2, 5.0),
                pingo.VccPin(self, 4, 5.0),
                pingo.VccPin(self, 17, 3.3)]

        pins += [pingo.GroundPin(self, n) for n in self.GROUNDS_LIST]

        pins += [pingo.PwmPin(self, location, gpio_id)
                 for location, gpio_id in self.PWM_PIN_MAP.items()]

        self._add_pins(pins)

    def cleanup(self):
        for pin in self.pins.values():
            if hasattr(pin, 'enabled') and pin.enabled:
                GPIO.cleanup(int(pin.gpio_id))
                pin.enabled = False

    def _set_pin_mode(self, pin, mode):
        # Cleans previous PWM mode
        if pin.mode == pingo.PWM:
        #if hasattr(pin, 'pwm_ctrl'):
            if pin.pwm_ctrl.is_running:
                pin.pwm_ctrl.stop()
                del pin.pwm_ctrl
        # Sets up new modes
        if mode == pingo.IN:
            GPIO.setup(int(pin.gpio_id), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        elif mode == pingo.OUT:
            GPIO.setup(int(pin.gpio_id), GPIO.OUT)
        elif mode == pingo.PWM:
            GPIO.setup(int(pin.gpio_id), GPIO.OUT)
            pin.pwm_ctrl = PwmWrapper(int(pin.gpio_id))

    def _set_pin_state(self, pin, state):
        rpi_state = GPIO.HIGH if state == pingo.HIGH else GPIO.LOW
        GPIO.output(int(pin.gpio_id), rpi_state)

    def _get_pin_state(self, pin):
        return pingo.HIGH if GPIO.input(int(pin.gpio_id)) else pingo.LOW

    def _get_pwm_duty_cycle(self, pin):
        return pin.pwm_ctrl.duty_cycle

    def _set_pwm_duty_cycle(self, pin, value):
        pin.pwm_ctrl.ChangeFrequency(value)


class RaspberryPiBPlus(RaspberryPi):

    # header_j8_location: gpio_id
    PWM_PIN_MAP = {
      # 1: 3.3v DC Power
      # 2: 5v DC Power
        3: 2, # SDA1, I2C
      # 4: 5v DC Power
        5: 3, # SCL1, I2C
      # 6: Ground
        7: 4, # GPIO_GCLK
        8: 14, # TXD0
      # 9: Ground
        10: 15, # RXD0
        11: 17, # GPIO_GEN0
        12: 18, # GPIO_GEN1
        13: 27, # GPIO_GEN2
      # 14: Ground
        15: 22, # GPIO_GEN3
        16: 23, # GPIO_GEN4
      # 17: 3.3v DC Power
        18: 24, # GPIO_GEN5
        19: 10, # SPI_MOSI
      # 20: Ground
        21: 9, # SPI_MOSO
        22: 25, # GPIO_GEN6
        23: 11, # SPI_CLK
        24: 8, # SPI_CE0_N
      # 25: Ground
        26: 7, # SPI_CE1_N
      # 27: ID_SD (I2C ID EEPROM)
      # 28: ID_SC (I2C ID EEPROM)
        29: 5,
      # 30: Ground
        31: 6,
        32: 12,
        33: 13,
      # 34: Ground
        35: 19,
        36: 16,
        37: 26,
        38: 20,
      # 39: Ground
        40: 21,
    }

    GROUNDS_LIST = [6, 9, 14, 20, 25, 30, 34, 39]

