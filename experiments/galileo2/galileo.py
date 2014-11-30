from pingo.board import Board, DigitalPin, AnalogPin, IN, OUT, HIGH, LOW
from pingo.board import AnalogInputCapable

DIGITAL_PINS_PATH = '/sys/class/gpio/'
DIGITAL_PIN_TEMPLATE = DIGITAL_PINS_PATH + 'gpio{pin}/{operation}'
DIGITAL_PIN_OPERATIONS = ('direction', 'value')

class Galileo2(Board):
    """
    Based on Rpi from commit 6a8bc000c4989df61dbeee01ec9ccfb85385555a
    """
    DIGITAL_PINS_PATH = '/sys/class/gpio/'
    ADC_PATH = '/proc/'

    DIGITAL_PIN_MODES = {IN: 'in', OUT: 'out'}
    DIGITAL_PIN_STATES = {HIGH: '1', LOW: '0'}
    
    # Galileo Gen2 # Do not trust
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

    def __init__(self):

        digital_pins = [
		DigitalPin(self, location, gpio)
                for location, gpio in 
		self.DIGITAL_PINS_MAP.items()
	]

        self._add_pins(digital_pins)


        for p in digital_pins:
	    print p.location, p.gpio_id

    def enable_pin(self, pin):
        if not hasattr(pin, 'enable'):
            pin.enable = False

        if not pin.enable: 
	    # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            with open(DIGITAL_PINS_PATH+'export', "wb", 0) as fp:
                fp.write(str(pin.gpio_id))
                # Magic Sleep. Less then 0.13 it doesn't works.
                #time.sleep(0.21)
            pin.enable = True

    def disable_pin(self, pin):
        if not hasattr(pin, 'enable'):
            pin.enable = False
        if pin.enable:
            # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            with open(DIGITAL_PINS_PATH + 'unexport', "wb", 0) as fp:
                fp.write(str(pin.gpio_id))
                # Magic Sleep. Less then 0.13 it doesn't works.
                #time.sleep(0.21)
            pin.enable = False

    def cleanup(self):
        for pin in self.pins:
            if pin.enable:
                pin.desable()

    def _render_path(self, pin, operation):
        error_mesg = 'Operation %r not in %r' % (operation, DIGITAL_PIN_OPERATIONS)
        assert operation in DIGITAL_PIN_OPERATIONS, error_mesg

        pin_context = {'pin': str(pin.gpio_id), 'operation': operation}
        pin_device = DIGITAL_PIN_TEMPLATE.format(**pin_context)
        return pin_device

    def _set_pin_mode(self, pin, mode):
	self.enable_pin(pin)
        pin_device = self._render_path(pin, 'direction')
        with open(pin_device, "wb") as fp:
            print pin_device, self.DIGITAL_PIN_MODES[mode]
            fp.write(self.DIGITAL_PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        pin_device = self._render_path(pin, 'value')
        with open(pin_device, "wb") as fp:
            print pin_device, self.DIGITAL_PIN_STATES[state]
            fp.write(self.DIGITAL_PIN_STATES[state])

