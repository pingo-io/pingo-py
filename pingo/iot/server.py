from flask import Flask
from flask_restful import Resource, Api
from pingo.board import AnalogInputCapable
import pingo
import sys


app = Flask(__name__)
api = Api(app)

board = pingo.detect.get_board()


class Main(Resource):
    def get(self):
        return {
            'board': repr(board),
            'pins': str(board.pins)
        }


class DigitalPins(Resource):
    def get(self, input_type):
        pins = board.pins()
        return {'pins': str(pins)}


class AnalogPins(Resource):
    def get(self, input_type):
        if issubclass(type(board), AnalogInputCapable):
            pins = str(board.digital_pins)
        else:
            pins = []
        return {'pins': str(pins)}


class Input(Resource):
    def get(self, input_type, pin):
        pin = board.pins[pin]
        pin.mode = pingo.IN
        return {'input': pin.state}


class AnalogOutput(Resource):
    def get(self, output_type, pin, signal):
        pin = board.pins[pin]
        pin.mode = pingo.OUT
        pin.value = signal
        return {'output': signal}


class DigitalOutput(Resource):
    def get(self, output_type, pin, signal):
        pin = board.pins[pin]
        pin.mode = pingo.OUT
        if signal:
            pin.high()
        else:
            pin.low()
        return {'output': signal}


api.add_resource(Main, '/')
api.add_resource(AnalogPins, '/analog')
api.add_resource(DigitalPins, '/digital')
api.add_resource(Input, '/<string:input_type>/<string:pin>')
api.add_resource(AnalogOutput, '/analog/<string:pin>/<float:signal>')
api.add_resource(DigitalOutput, '/digital/<string:pin>/<int:signal>')


if __name__ == '__main__':
    try:
        kwargs = {'host': sys.argv[1]}
    except:
        kwargs = {}
    app.run(debug=True, **kwargs)
