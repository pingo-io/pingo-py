import time
import unittest

from pingo.parts import Switch


class FakeDigitalPin(object):
    def __init__(self):
        self.mode = 'IN'
        self.state = 'LOW'


class TestSwitch(unittest.TestCase):
    def setUp(self):
        self.pin = FakeDigitalPin()
        self.my_switch = Switch(self.pin)
        self.my_switch.test_list = []

    def test_run_down_callback(self):
        def callback_down():
            self.my_switch.test_list += ['down']
        self.my_switch.set_callback_down(callback_down)

        self.my_switch.start()
        time.sleep(.1)
        self.pin.state = 'HIGH'
        time.sleep(.1)
        self.pin.state = 'LOW'
        time.sleep(.1)
        self.pin.state = 'HIGH'
        time.sleep(.1)
        self.my_switch.stop()

        self.assertEqual(self.my_switch.test_list, ['down'])

    def test_run_both_callback(self):
        def callback_down():
            self.my_switch.test_list += ['down']

        def callback_up():
            self.my_switch.test_list += ['up']

        self.my_switch.set_callback_down(callback_down)
        self.my_switch.set_callback_up(callback_up)

        self.my_switch.start()
        time.sleep(.1)
        self.pin.state = 'HIGH'
        time.sleep(.1)
        self.pin.state = 'LOW'
        time.sleep(.1)
        self.pin.state = 'HIGH'
        time.sleep(.1)

        self.my_switch.stop()

        self.assertEqual(self.my_switch.test_list, ['up', 'down', 'up'])

if __name__ == '__main__':
    unittest.main()
