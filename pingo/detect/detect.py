import os
import glob
import platform

import pingo


class DetectionFailed(Exception):
    def __init__(self):
        super(DetectionFailed, self).__init__()
        self.message = 'Pingo is not able to detect your board.'


def _read_cpu_info():
    with open('/proc/cpuinfo', 'r') as fp:
        for line in fp:
            if line.startswith('Hardware'):
                key, value = tuple(line.split(':'))
                return value.strip()


def _find_arduino_dev(system):
    if system == 'Linux':
        # TODO: filter possible devices with glob
        devices = []
        for dev in os.listdir('/dev/'):
            if ('ttyUSB' in dev) or ('ttyACM' in dev):
                devices.append(dev)
        if len(devices) == 1:
            return os.path.join(os.path.sep, 'dev', devices[0])

    elif system == 'Darwin':
        devices = glob.glob('/dev/tty.usbmodem*')
        if len(devices) == 1:
            return os.path.join(os.path.sep, 'dev', devices[0])
    return False

def MyBoard():
    machine = platform.machine()
    system = platform.system()

    if machine == 'x86_64':
        if system in ['Linux', 'Darwin']:
            # TODO: Try to find 'Arduino' inside dmesg output
            device = _find_arduino_dev(system)
            if device:
                return pingo.arduino.ArduinoFirmata(device)

        print('Using GhostBoard...')
        # TODO decide which board return
        return pingo.ghost.GhostBoard()

    if machine == 'armv6l':
        print('Using RaspberryPi...')
        return pingo.rpi.RaspberryPi()

    if machine == 'armv7l':

        if system == 'Linux':

            hardware = _read_cpu_info()
            lsproc = os.listdir('/proc/')
            adcx = [p for p in lsproc if p.startswith('adc')]

            if len(adcx) == 6:
                print('Using PcDuino...')
                return pingo.pcduino.PcDuino()

            if 'Generic AM33XX' in hardware:
                print('Using Beaglebone...')
                return pingo.bbb.BeagleBoneBlack()

            if 'SECO i.Mx6 UDOO Board' in hardware:
                print('Using Udoo...')
                return pingo.udoo.Udoo()

        raise DetectionFailed()
