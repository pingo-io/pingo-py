import ctypes

mraa = None

try:
   import mraa as mraa
except:
   pass

import pingo

class Galileo2(pingo.Board, pingo.AnalogInputCapable):

    PIN_MODES = {
        pingo.IN: mraa.DIR_IN,
        pingo.OUT: mraa.DIR_OUT,
    }

    PIN_STATES = {                       
        pingo.HIGH: 1,         
        pingo.LOW: 0,                 
    }

    def __init__(self):
        self._add_pins(
            [pingo.DigitalPin(self, location)
            for location in range(1, 14)] +
            [pingo.AnalogPin(self, 'A'+location, 12)
            for location in '012345']
        )

	self.mraa_pins = {
            location: mraa.Gpio(location)
            for location in range(1, 14)
        }

	self.mraa_analogs = {
            'A'+location: mraa.Aio(int(location))
            for location in '012345'
        }

    def _set_pin_mode(self, pin, mode):
        self.mraa_pins[pin.location].dir(self.PIN_MODES[mode])

    def _set_pin_state(self, pin, state):
        self.mraa_pins[pin.location].write(self.PIN_STATES[state])

    def _get_pin_state(self, pin):
        value = self.mraa_pins[pin.location].read()
        return pingo.HIGH if value == 1 else pingo.LOW

    def _get_pin_value(self, pin):
       return self.mraa_analogs[pin.location].read()

    def _set_analog_mode(self, pin, mode):
        pass
