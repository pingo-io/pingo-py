from pingo.board import Board, DigitalPin, AnalogPin, IN, OUT, HIGH, LOW
from pingo.board import AnalogInputCapable


class Galileo2(Board, AnalogInputCapable):
    """
    pcDuino board (works on V1 and V3)
    """
    DIGITAL_PINS_PATH = '/sys/class/gpio/'
    ADC_PATH = '/proc/'

    DIGITAL_PIN_MODES = {IN: '0', OUT: '1'}
    DIGITAL_PIN_STATES = {HIGH: '1', LOW: '0'}

    DIGITAL_PINS_MAP = {
	0: 11,
	1: 12,
	2: 13,
	3: 14,
	4: 6,
	5: 0,
	6: 1,
	7: 38,
	8: 40,
	9: 4,
	10: 10,
	11: 5,
	13: 15,
	14: 7,
    }

    ANALOG_PIN_RESOLUTIONS = [12, 12, 12, 12, 12, 12]

    def __init__(self):
        self._add_pins(

            [
		DigitalPin(self, location, gpio)
                for location, gpio in 
		self.DIGITAL_PINS_MAP.items()
	    ] +

            [AnalogPin(self, 'A%s' % location, resolution=bits)
                for location, bits in enumerate(self.ANALOG_PIN_RESOLUTIONS)])

    def _set_pin_mode(self, pin, mode):
        err_msg = '%r not in %r' % (mode, self.DIGITAL_PIN_MODES)
        assert mode in self.DIGITAL_PIN_MODES, err_msg
        sys_string = self.DIGITAL_PINS_PATH + 'mode/gpio%s' % pin.location
        with open(sys_string, 'w') as fp:
            fp.write(self.DIGITAL_PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        sys_string = self.DIGITAL_PINS_PATH + 'pin/gpio%s' % pin.location
        with open(sys_string, 'w') as fp:
            fp.write(self.DIGITAL_PIN_STATES[state])

    def _get_pin_state(self, pin):
        sys_string = self.DIGITAL_PINS_PATH + 'pin/gpio%s' % pin.location
        with open(sys_string, 'r') as fp:
            state = fp.read().strip()
            return HIGH if state == '1' else LOW

    def _set_analog_mode(self, pin, mode):
        pass

    def _get_pin_value(self, pin):
        sys_string = self.ADC_PATH + 'adc%s' % pin.location[1:]  # eg. A5
        with open(sys_string) as fp:
            fp.seek(0)
            return int(fp.read(16).split(':')[1])
