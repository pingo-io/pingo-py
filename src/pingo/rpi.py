import time

from pingo.board import Board, DigitalPin, GroundPin, VddPin
from pingo.board import INPUT, OUTPUT


# connector_p1_location: gpio_id
DIGITAL_PIN_MAP = {
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

GROUND_PINS = (6, 9, 14, 20, 25)
#VCC_PINS = (1, 2, 4, 17)

DIGITAL_PINS_PATH = '/sys/class/gpio/'
DIGITAL_PIN_TEMPLATE = DIGITAL_PINS_PATH + 'gpio{pin}/{operation}'
DIGITAL_PIN_MODES = {INPUT: 'in', OUTPUT: 'out'}
DIGITAL_PIN_OPERATIONS = ('direction', 'value')


class RaspberryPi(object):
    """
    Reference:
    http://falsinsoft.blogspot.com.br/2012/11/access-gpio-from-linux-user-space.html
    """

    def __init__(self):

	pins = [
	    VddPin(self, 1, 3.3),
	    VddPin(self, 2, 5.0),
	    VddPin(self, 4, 5.0),
	    VddPin(self, 17, 3.3),
	]

	pins += [GroundPin(self, n) for n in [6, 9, 14, 20, 25]]

	pins += [DigitalPin(self, location, gpio_id)
		    for location, gpio_id in DIGITAL_PIN_MAP.items()]

	self.add_pins(pins)

    def add_pins(self, pins):
        self.pins = {}
        for pin in pins:
            self.pins[pin.location] = pin

    def enable_pin(self, pin):
        if not pin.enable:
            # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            with open(DIGITAL_PINS_PATH+'export', "wb", 0) as fp:
                fp.write(pin.gpio_id)
                # Magic Sleep. Less then 0.13 it doesn't works.
                #time.sleep(0.21)
            pin.enable = True

    def disable_pin(self, pin):
        if pin.enable:
            # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            with open(DIGITAL_PINS_PATH+'export', "wb", 0) as fp:
                fp.write(pin.gpio_id)
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

    def set_pin_mode(self, pin, mode):
        pin_device = self._render_path(pin.gpio_id, 'direction')
        with open(pin_device, "wb") as fp:
            fp.write(str(DIGITAL_PIN_MODES[mode]))

    def set_pin_state(self, pin, state):
        pin_device = self._render_path(pin.gpio_id, 'value')
        with open(pin_device, "wb") as fp:
            fp.write(str(state))

