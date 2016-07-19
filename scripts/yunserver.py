#!/usr/bin/env python
import random

from flask import Flask
from flask import make_response, abort

app = Flask(__name__)

"""
Arduino Yun REST-API dev-server.

This server mimics Arduino's Examples > Bridge
http://arduino.cc/en/Tutorial/Bridge
http://arduino.cc/en/Tutorial/Bridge?action=sourceblock&num=13
"""


@app.errorhandler(404)
def not_found(error):
        return make_response('error', 404)


@app.route('/')
def index():
    return "Pingo's Arduino Yun REST-API dev-server."


@app.route('/arduino/mode/<int:pin>/<mode>')
def mode(pin, mode):
    if mode not in ['input', 'output'] or pin not in range(14):
        abort(404)
    umode = mode.upper()
    return "Pin D{pin} configured as {umode}!".format(**locals())


@app.route('/arduino/digital/<int:pin>', defaults={'value': None})
@app.route('/arduino/digital/<int:pin>/<value>')
def digital(pin, value):
    if value is None:
        uvalue = random.choice((0, 1))
    else:
        uvalue = 1 if value else 0
    return "Pin D{pin} set to {uvalue}".format(**locals())


@app.route('/arduino/analog/<int:pin>', defaults={'value': None})
@app.route('/arduino/analog/<int:pin>/<int:value>')
def analog(pin, value):
    if value is None:
        if pin in range(6):
            uvalue = random.choice(range(1024))
            rw = "reads"
        else:
            abort(404)
    else:
        if pin in [3, 5, 6, 9, 10, 11, 13]:
            uvalue = value % 256
            rw = "set to"
        else:
            abort(404)
    return "Pin A{pin} {rw} analog {uvalue}".format(**locals())


if __name__ == '__main__':
    app.run(debug=True)
