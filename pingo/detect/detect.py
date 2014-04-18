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

    if machine == 'armv7a':
        print 'Using Udoo...'
        return pingo.udoo.Udoo()

    raise DetectionFailed()

