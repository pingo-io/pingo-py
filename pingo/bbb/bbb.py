import pingo

GPIO = None


class BeagleBoneBlack(pingo.Board):
    # TODO: use labels as in the docs (https://github.com/adafruit/adafruit-beaglebone-io-python)

    PINS = {
        'P8_3':  38,
        'P8_4':  39,
        'P8_5':  34,
        'P8_6':  35,
        'P8_7':  66,
        'P8_8':  67,
        'P8_9':  69,
        'P8_10': 68,
        'P8_11': 45,
        'P8_12': 44,
        'P8_13': 23,
        'P8_14': 26,
        'P8_15': 47,
        'P8_16': 46,
        'P8_17': 27,
        'P8_18': 65,
        'P8_19': 22,
        'P8_20': 63,
        'P8_21': 62,
        'P8_22': 37,
        'P8_23': 36,
        'P8_24': 33,
        'P8_25': 32,
        'P8_26': 61,
        'P8_27': 86,
        'P8_28': 88,
        'P8_29': 87,
        'P8_30': 89,
        'P8_31': 10,
        'P8_32': 11,
        'P8_33': 9,
        'P8_34': 81,
        'P8_35': 8,
        'P8_36': 80,
        'P8_37': 78,
        'P8_38': 79,
        'P8_39': 76,
        'P8_40': 77,
        'P8_41': 74,
        'P8_42': 75,
        'P8_43': 72,
        'P8_44': 73,
        'P8_45': 70,
        'P8_46': 71,
        'P9_11': 30,
        'P9_12': 60,
        'P9_13': 31,
        'P9_14': 40,
        'P9_15': 48,
        'P9_16': 51,
        'P9_17': 4,
        'P9_18': 5,
        'P9_21': 3,
        'P9_22': 2,
        'P9_23': 49,
        'P9_24': 15,
        'P9_25': 117,
        'P9_26': 14,
        'P9_27': 125,
        'P9_28': 123,
        'P9_29': 121,
        'P9_30': 122,
        'P9_31': 120,
        'P9_41': 20,
        'P9_42': 7,
    }

    VCC_PINS = {
            'P9_3': 3.3,
            'P9_4': 3.3,
            'P9_5': 5,
            'P9_6': 5,
            'P9_7': 5,
            'P9_8': 5,
            'P9_32': 5  # VDD_ADC
    }

    GND_PINS = ['P8_1', 'P8_2', 'P9_1', 'P9_2', 'P9_34', 'P9_43', 'P9_44',
                'P9_45', 'P9_46']

    ANALOG_PINS = {
        'P9_33': 'AIN4',
        'P9_35': 'AIN6',
        'P9_36': 'AIN5',
        'P9_37': 'AIN2',
        'P9_38': 'AIN3',
        'P9_39': 'AIN0',
        'P9_40': 'AIN1',
    }

    # TODO: PWR_BUT, SYS_RESET, I2C2_SCL, I2C2_SDA

    _import_error_msg = 'pingo.bbb.BeagleBoneBlack requires AdafruitBBIO installed'

    def __init__(self):
        global GPIO
        try:
            import AdafruitBBIO.GPIO as GPIO
        except ImportError:
            raise ImportError(self._import_error_msg)

        super(BeagleBoneBlack, self).__init__()

        self.PIN_MODES = {
            pingo.IN: GPIO.IN,
            pingo.OUT: GPIO.OUT,
        }

        self.PIN_STATES = {
            pingo.HIGH: GPIO.HIGH,
            pingo.LOW: GPIO.LOW,
        }

        gpio_pins = [pingo.Pin(self, location, gpio_id)
                         for location, gpio_id in self.PINS]
        ground_pins = [pingo.GroundPin(self, location)
                           for location in self.GND_PINS]
        vcc_pins = [pingo.VccPin(self, location, voltage)
                        for location, voltage in self.VCC_PINS]

        self._add_pins(gpio_pins + ground_pins + vcc_pins)

    def cleanup(self):
        pass

    def _set_digital_mode(self, pin, mode):
        GPIO.setup(pin.location, self.PIN_MODE[mode])

    def _set_pin_state(self, pin, state):
        GPIO.output(pin.location, self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        return pingo.HIGH if GPIO.input(pin.location) else pingo.LOW
