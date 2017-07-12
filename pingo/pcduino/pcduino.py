from pingo.board import Board, DigitalPin, AnalogPin
from pingo.board import AnalogInputCapable
from pingo.board import State, Mode


class PcDuino(Board, AnalogInputCapable):
    """
    pcDuino board (works on V1 and V3)
    """
    DIGITAL_PINS_PATH = '/sys/devices/virtual/misc/gpio/'
    ADC_PATH = '/proc/'

    DIGITAL_PIN_MODES = {Mode.IN: '0', Mode.OUT: '1'}
    DIGITAL_PIN_STATES = {State.HIGH: '1', State.LOW: '0'}
    LEN_DIGITAL_PINS = 14
    ANALOG_PIN_RESOLUTIONS = [6, 6, 12, 12, 12, 12]

    def __init__(self):
        self._add_pins(
            [DigitalPin(self, location)
                for location in range(self.LEN_DIGITAL_PINS)] +
            [AnalogPin(self, 'A%s' % location, resolution=bits)
                for location, bits in enumerate(self.ANALOG_PIN_RESOLUTIONS)])

    def _set_digital_mode(self, pin, mode):
        err_msg = '%r not in %r' % (mode, self.DIGITAL_PIN_MODES)
        assert mode in self.DIGITAL_PIN_MODES, err_msg
        sys_string = self.DIGITAL_PINS_PATH + 'mode/gpio%s' % pin.location
        with open(sys_string, 'w') as fp:
            fp.write(self.DIGITAL_PIN_MODES[mode])

    def _set_analog_mode(self, pin, mode):
        pass

    def _set_pin_state(self, pin, state):
        sys_string = self.DIGITAL_PINS_PATH + 'pin/gpio%s' % pin.location
        with open(sys_string, 'w') as fp:
            fp.write(self.DIGITAL_PIN_STATES[state])

    def _get_pin_state(self, pin):
        sys_string = self.DIGITAL_PINS_PATH + 'pin/gpio%s' % pin.location
        with open(sys_string, 'r') as fp:
            state = fp.read().strip()
            return State.HIGH if state == '1' else State.LOW

    def _get_pin_value(self, pin):
        sys_string = self.ADC_PATH + 'adc%s' % pin.location[1:]  # eg. A5
        with open(sys_string) as fp:
            fp.seek(0)
            return int(fp.read(16).split(':')[1])
