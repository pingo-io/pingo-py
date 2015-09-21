from bottle import Bottle
from pingo.board import AnalogPin
import json
import pingo
import sys


app = Bottle(__name__)
board = pingo.detect.get_board()


@app.route('/')
def main():
    pins = {key: repr(value) for key, value in board.pins}
    return {
        'board': repr(board),
        'pins': json.dumps(pins)
    }


@app.route('/mode/<mode>/<pin>')
def mode(mode, pin):
    assert mode in ('input', 'output')
    mode = pingo.IN if 'input' else pingo.OUT
    pin = board.pins[pin]
    pin.mode = mode


@app.route('/analog')
def analog_pins():
    # TODO: find a better way to check if the pin is analog
    pins = {key: value for key, value in board.pins
                if issubclass(type(board), AnalogPin)}
    return {'pins': str(pins)}


@app.route('/analog/<pin>')
def analog_input(pin):
    pin = board.pins[pin]
    pin.mode = pingo.IN
    return {'input': pin.state}


@app.route('/analog/<pin>/<float:signal>')
def analog_output(pin, signal):
    pin = board.pins[pin]
    pin.mode = pingo.OUT
    pin.value = signal
    return {'output': signal}


@app.route('/digital')
def digital_pins():
    pins = board.pins()
    return {'pins': str(pins)}


@app.route('/digital/<pin>')
def digital_input(pin):
    pin = board.pins[pin]
    pin.mode = pingo.IN
    return {'input': pin.state}


@app.route('/digtal/<pin>/<int:signal>')
def digital_output(pin, signal):
    pin = board.pins[pin]
    pin.mode = pingo.OUT
    pin.high() if signal else pin.low()
    return {'output': signal}


if __name__ == '__main__':
    try:
        kwargs = {'host': sys.argv[1]}
    except IndexError:
        kwargs = {}
    app.run(debug=True, **kwargs)
