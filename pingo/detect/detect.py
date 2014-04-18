import os
import platform

import pingo

class DetectionFailed(Exception):
    def __init__(self):
        super(DetectionFailed, self).__init__()
        self.message = 'Pingo is not able to detect your board.'


def MyBoard():
    machine = platform.machine()

    if machine == 'x86_64':
        print 'Using GhostBoard...'
        return pingo.ghost.GhostBoard()

    if machine == 'armv6l':
        print 'Using RaspberryPi...'
        return pingo.rpi.RaspberryPi()

    if machine == 'armv7l':
        lsproc = os.listdir('/proc/')
        adcx = [p for p in lsproc if p.startswith('adc')]

        if len(adcx) == 6:
            print 'Using PcDuino...'
            return pingo.pcduino.PcDuino()

        if len(adcx) == 0:
            print 'Using Udoo...'
            return pingo.udoo.Udoo()

    raise DetectionFailed()

