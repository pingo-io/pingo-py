import time

from pingo.board import Board, DigitalPin, GroundPin, VddPin
from pingo.board import INPUT, OUTPUT


DIGITAL_PIN_MAP = {
    # pin_number: gpio_id
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


class RaspberryPi(Board):
    """
    Reference:
    http://falsinsoft.blogspot.com.br/2012/11/access-gpio-from-linux-user-space.html
    """

    def __init__(self):
        Board.__init__(self)

        # Exports all pins
        for n in DIGITAL_PIN_MAP.values():
            # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            with open(DIGITAL_PINS_PATH+'export', "wb", 0) as fp:
                fp.write(str(n))
            # Magic Sleep. Less then 0.13 it doesn't works.
            time.sleep(0.21)

        digital_pins = [
            DigitalPin(self, number, gpio_id)
                for number, gpio_id in DIGITAL_PIN_MAP.items()
        ]

        gnd_pins = [
            GroundPin(self, n) for n in GROUND_PINS
        ]

        vcc_pins = [
           VddPin(self, 1, "3.3V"),
           VddPin(self, 2, "5V"),
           VddPin(self, 3, "5V"),
           VddPin(self, 17, "3.3V"),
        ]

        pins = digital_pins + gnd_pins + vcc_pins
        self.add_pins(pins)

    def cleanup(self):
        for n in DIGITAL_PIN_MAP.values():
            # 3rd arg: buffer_size=0 (a.k.a AutoFlush)
            try:
                with open(DIGITAL_PINS_PATH+'unexport', "wb", 0) as fp:
                    fp.write(str(n))
                # Magic Sleep. Less then 0.13 it doesn't works.
                time.sleep(0.21)
            except IOError as e:
                print(repr(e))
                print(repr(n))

    def _render_path(self, pin, operation):
        error_mesg = 'Operation %r not in %r' % (operation, DIGITAL_PIN_OPERATIONS)
        assert operation in DIGITAL_PIN_OPERATIONS, error_mesg

        pin_context = {'pin': str(pin.gpio_id), 'operation': operation}
        pin_device = DIGITAL_PIN_TEMPLATE.format(**pin_context)
        return pin_device

    def set_pin_mode(self, pin, mode):
        pin_device = self._render_path(pin, 'direction')
        with open(pin_device, "wb") as fp:
            fp.write(str(DIGITAL_PIN_MODES[mode]))

    def set_pin_state(self, pin, state):
        pin_device = self._render_path(pin, 'value')
        with open(pin_device, "wb") as fp:
            fp.write(str(state))

