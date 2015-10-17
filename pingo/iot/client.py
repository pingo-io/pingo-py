import json
import pingo
try:
    # Python 2.7
    from urllib2 import urlopen
except ImportError:
    # Python 3+
    from urrlib.requests import urlopen


class HTTPBoard(pingo.Board):
    """
    """

    def __init__(self, server):
        self.server = server
        response = urlopen(server)
        if response.code != 200:
            raise Exception(u'HTTPBoard not found on server {}'.format(server))
        response = json.load(response)
        pins = json.loads(response['pins'])
        gpio_pins = []
        ground_pins = []
        vcc_pins = []
        pwm_pins = []
        for pin, value in pins.items():
            # TODO: serialize the pin (and/or the board) to do this in a better way
            if 'GroundPin' in value:
                ground_pins.append(pingo.GroundPin(self, pin))
            elif 'VccPin' in value:
                voltage = float(value[:-2].split(' ')[1])
                vcc_pins.append(pingo.VccPin(self, pin, voltage))
            elif 'PwmPin' in value:
                gpio_id = value.split(' ')[1].split('@')[0]
                pwm_pins.append(pingo.PwmPin(self, pin, gpio_id))
            elif 'DigitalPin' in value:
                gpio_id = value.split(' ')[1].split('@')[0]
                gpio_pins.append(pingo.DigitalPin(self, pin, gpio_id))
        self._add_pins(ground_pins + vcc_pins + gpio_pins + pwm_pins)

    def _set_digital_mode(self, pin, mode):
        mode = 'input' if pingo.IN else 'output'
        url = '{server}mode/{mode}/{pin}'.format(server=self.server,
                                                 mode=mode, pin=pin.location)
        urlopen(url)

    def _set_pin_state(self, pin, state):
        mode = 'analog' if pin.is_analog else 'digital'
        state = 1 if state == pingo.HIGH else 0
        url = '{server}{mode}/{pin}/{state}'.format(server=self.server, mode=mode,
                                                    pin=str(pin.location),
                                                    state=str(state))
        print(url)
        response = urlopen(url)
        if response.code != 200:
            message = u'Pin {} could not be set to {}. HTTPBoard response: {}'
            message.format(repr(pin), state, response.code)
            raise Exception(message)

    def _get_pin_state(self, pin):
        mode = 'analog' if pin.is_analog else 'digital'
        url = '{server}{mode}/{pin}'.format(server=self.server, mode=mode,
                                            pin=pin.location)
        response = urlopen(url)
        if response.code != 200:
            message = u'Pin {} could not be read: HTTPBoard response: {}'
            message.format(repr(pin), response.code)
            raise Exception(message)
        return response['input']
