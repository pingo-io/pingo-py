import os
from pingo.board import Board, DigitalPin, AnalogPin, IN, OUT, HIGH, LOW
from pingo.board import AnalogInputCapable


class PcDuinoV1(Board, AnalogInputCapable):
    """
    pcDuino v1 board
    """
    # /sys/class/gpio/gpio40/ --> Arduino pin #13
    DIGITAL_PINS_PATH = '/sys/devices/virtual/misc/gpio/'
    ADC_PATH = '/proc/'

    DIGITAL_PIN_MODES = {IN: '0', OUT: '1'}
    DIGITAL_PIN_STATES = {HIGH:'1', LOW:'0'}
    LEN_DIGITAL_PINS = 14
    ANALOG_PIN_RESOLUTIONS = [6, 6, 12, 12, 12, 12]

    def __init__(self):
        self._add_pins([DigitalPin(self, location)
                       for location in range(LEN_DIGITAL_PINS)] +
                      [AnalogPin(self, 'A%s' % location, resolution=bits)
                       for location, bits in enumerate(ANALOG_PIN_RESOLUTIONS)])

    def _set_pin_mode(self, pin, mode):
        assert mode in DIGITAL_PIN_MODES, '%r not in %r' % (mode, DIGITAL_PIN_MODES)
        with open(DIGITAL_PINS_PATH+'mode/gpio%s' % pin.location, 'w') as fp:
            fp.write(DIGITAL_PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        with open(DIGITAL_PINS_PATH+'pin/gpio%s' % pin.location, 'w') as fp:
            fp.write(DIGITAL_PIN_STATES[state])

    def _get_pin_state(self, pin):
        with open(DIGITAL_PINS_PATH+'pin/gpio%s' % pin.location, 'r') as fp:
            state = fp.read().strip()
            return HIGH if state == '1' else LOW

    def _set_analog_mode(self, pin, mode):
        pass

    def _get_pin_value(self, pin):
        adc_id = pin.location[-1]
        with open(ADC_PATH+'adc%s' % adc_id) as fp:
            fp.seek(0)
            return int(fp.read(16).split(':')[1])


class PcDuinoV3(Board, AnalogInputCapable):
    """
    pcDuino v3 board
    """
    DIGITAL_PINS_PATH =  os.path.normpath('/sys/devices/virtual/misc/mode/')
    ADC_PATH = os.path.normpath('/proc/')

    DIGITAL_PIN_MODES = {IN: '0', OUT: '1'}
    DIGITAL_PIN_STATES = {HIGH:'1', LOW:'0'}
    LEN_DIGITAL_PINS = 14
    ANALOG_PIN_RESOLUTIONS = [6, 6, 12, 12, 12, 12]

    def __init__(self):
        self._add_pins([DigitalPin(self, location)
                       for location in range(LEN_DIGITAL_PINS)] +
                      [AnalogPin(self, 'A%s' % location, resolution=bits)
                       for location, bits in enumerate(ANALOG_PIN_RESOLUTIONS)])

    def _set_pin_mode(self, pin, mode):
        assert mode in DIGITAL_PIN_MODES, '%r not in %r' % (mode, DIGITAL_PIN_MODES)
        with open(DIGITAL_PINS_PATH+'/gpio%s' % pin.location, 'w') as fp:
            fp.write(DIGITAL_PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        with open(DIGITAL_PINS_PATH+'/gpio%s' % pin.location, 'w') as fp:
            fp.write(DIGITAL_PIN_STATES[state])

    def _get_pin_state(self, pin):
        with open(DIGITAL_PINS_PATH+'pin/gpio%s' % pin.location, 'r') as fp:
            state = fp.read().strip()
            return HIGH if state == '1' else LOW

    def _set_analog_mode(self, pin, mode):
        pass

    def _get_pin_value(self, pin):
        adc_id = pin.location[-1]
        with open(ADC_PATH+'adc%s' % adc_id) as fp:
            fp.seek(0)
            return int(fp.read(16).split(':')[1])

