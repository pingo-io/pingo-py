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
        def test_callback():
            self.test_list += ['down']
        self.my_switch.set_callback_down(test_callback)

        self.my_switch.run()
        time.sleep(0.005)
        self.pin.state = 'HIGH'
        time.sleep(0.005)
        self.pin.state = 'LOW'
        time.sleep(0.005)
        self.pin.state = 'HIGH'
        self.my_switch.stop()
        self.my_switch.join()

        self.assertEqual(self.my_switch.test_list, ['down'])

    def test_run_both_callback(self):
        def test_down():
            self.test_list += ['down']

        def test_up():
            self.test_list += ['up']

        self.my_switch.set_callback_down(test_down)
        self.my_switch.set_callback_up(test_up)

        self.my_switch.run()
        time.sleep(0.005)
        self.pin.state = 'HIGH'
        time.sleep(0.005)
        self.pin.state = 'LOW'
        time.sleep(0.005)
        self.pin.state = 'HIGH'

        self.my_switch.stop()
        self.my_switch.join()

        self.assertEqual(self.my_switch.test_list, ['up','down', 'up'])

if __name__ == '__main__':
    unittest.main()

