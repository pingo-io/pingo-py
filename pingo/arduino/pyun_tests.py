# coding: utf-8

"""

    >>> from pyun import *
    >>> yun = YunBridge('192.168.2.9')
    >>> yun.pinMode(13, INPUT)
    'input'
    >>> yun.digitalRead(13)
    0
    >>> yun.digitalWrite(13, 1)
    1
    >>> yun.digitalWrite(13, 0)
    0
    >>> 0 <= yun.analogRead(5) < 1024
    True


"""

import doctest
doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
