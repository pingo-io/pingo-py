from pingo.board import Board


class BeagleBoneBlack(Board):

    def __init__(self):
        global GPIO
        try:
            import Adafruit_BBIO.GPIO as GPIO
        except ImportError:
            raise ImportError(
                    'pingo.bbb.BeagleBoneBlack requires Adafruit_BBIO installed'
                    )

        super(BeagleBoneBlack, self).__init__()

    def cleanup(self):
        pass

    def _set_digital_mode(self, pin, mode):
        pass

    def _set_pin_state(self, pin, state):
        pass

    def _get_pin_state(self, pin):
        pass
