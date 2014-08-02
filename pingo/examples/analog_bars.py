import pingo
import time

b = pingo.detect.MyBoard()
p = b.pins['A0']
p.mode = pingo.ANALOG

def bar(pin):
    print "*" * int(pin.ratio() * 70)

for i in xrange(10):
    bar(p)
    time.sleep(0.05)

