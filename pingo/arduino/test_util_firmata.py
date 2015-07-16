import unittest

from util_firmata import pin_list_to_board_dict


class FirmataCapabilityDetect(unittest.TestCase):

    def test_capability_response(self):
        test_layout = {
            'digital': (0, 1),
            'analog': (0,),  # Analog are numbered from zero
            'pwm': (1,),
            'i2c': (2,),
            'disabled': (0,),
        }

        # Eg: (127)
        unavailible_pin = [
            0x7F,  # END_SYSEX (Pin delimiter)
        ]

        # Eg: (0, 1, 1, 1, 3, 8, 4, 14, 127)
        digital_pin = [
            0x00,  # INPUT
            0x01,
            0x01,  # OUTPUT
            0x01,
            0x03,  # PWM
            0x08,
            0x7F,  # END_SYSEX (Pin delimiter)
        ]

        # Eg. (0, 1, 1, 1, 4, 14, 127)
        analog_pin = [
            0x00,  # INPUT
            0x01,
            0x01,  # OUTPUT
            0x01,
            0x02,  # ANALOG
            0x0A,
            0x06,  # I2C
            0x01,
            0x7F,  # END_SYSEX (Pin delimiter)
        ]

        data_arduino = list(
            # [0x6C]  # CAPABILITY_RESPONSE
            unavailible_pin
            + digital_pin
            + analog_pin
        )

        pinmap = pin_list_to_board_dict(data_arduino)
        for key in test_layout.keys():
            self.assertEqual(pinmap[key], test_layout[key])

if __name__ == '__main__':
    unittest.main()
