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
        url = self.server + '/mode'
        mode = 'input' if pingo.IN else 'output'
        urlopen(url + '/' + mode + '/' + str(pin.location))

    def _set_pin_state(self, pin, state):
        url = self.server
        if pin.is_analog:
            url += '/analog'
        else:
            url += '/digital'
        response = urlopen(url + '/' + str(pin.location) + '/' + str(state))
        if response.code != 200:
            message = u'Pin {} could not be set to {}: HTTPBoard response: {}'
            message.format(repr(pin), state, response.code)
            raise Exception(message)

    def _get_pin_state(self, pin):
        url = self.server
        if pin.is_analog:
            url += '/analog'
        else:
            url += '/digital'
        response = urlopen(url + '/' + str(pin.location))
        if response.code != 200:
            message = u'Pin {} could not be read: HTTPBoard response: {}'
            message.format(repr(pin), response.code)
            raise Exception(message)
        return response['input']
