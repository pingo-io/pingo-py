from pingo.board import Board, DigitalPin, GroundPin, VddPin
from pingo.board import INPUT, OUTPUT


DIGITAL_PIN_MAP = {
    3: 2, 5: 3, 7: 4, 8: 14, 10: 15, 11: 17, 12: 18, 13: 27, 15: 22,
    16: 23, 18: 24, 19: 10, 21: 9, 22: 25, 23: 11, 24: 8, 26: 7,
}
GROUND_PINS = (6, 9, 14, 20, 25)
VCC_PINS = (1, 2, 4, 17)

DIGITAL_PINS_PATH = '/sys/class/gpio/'
DIGITAL_PIN_TEMPLATE = DIGITAL_PINS_PATH + 'gpio{pin}/{operation}'
DIGITAL_PIN_MODES = {INPUT: 'in', OUTPUT: 'out'}
DIGITAL_PIN_OPERATIONS = ('direction', 'value')


class RaspberryPi(Board):
    """
    Reference:
    http://falsinsoft.blogspot.com.br/2012/11/access-gpio-from-linux-user-space.html
    """

    def __init__(self):
        digital_pins = [(n, DigitalPin(self, n))
                            for n in DIGITAL_PIN_MAP.keys()]
        gnd_pins = [(n, GroundPin(self)) for n in GROUND_PINS]
        vcc_pins = [
           (1, VddPin(self, "3.3V")),
           (2, VddPin(self, "5V")),
           (4, VddPin(self, "5V")),
           (17, VddPin(self, "3.3V")),
        ]

        pins = digital_pins + gnd_pins + vcc_pins
        self.add_pins(pins)

        for n, pin in pins:
            fp = open(DIGITAL_PINS_PATH+'export', "wb")
            fp.write(n)
            fp.close()

    def __del__(self):
        pins = DIGITAL_PIN_MAP.keys() + list(GROUND_PINS) + list(VCC_PINS)

        for n in pins:
            fp = open(DIGITAL_PINS_PATH+'unexport', "wb")
            fp.write(n)
            fp.close()

    def _render_path(self, pin, operation):
        error_mesg = 'Operation %r not in %r' % (operation, DIGITAL_PIN_OPERATIONS)
        assert operation in DIGITAL_PIN_OPERATIONS, error_mesg

        pin_context = {'pin': str(pin.logical_id), 'operation': operation}
        pin_device = DIGITAL_PIN_TEMPLATE.format(**pin_context)
        return pin_device

    def set_pin_mode(self, pin, mode):
        pin_device = self._render_path(pin, 'direction')
        with open(pin_device, "wb") as fp:
            fp.write(DIGITAL_PIN_MODES[mode])

    def set_pin_state(self, pin, state):
        pin_device = self._render_path(pin, 'value')
        with open(pin_device, "wb") as fp:
            fp.write(state)

