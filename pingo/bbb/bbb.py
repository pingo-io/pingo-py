from pingo.board import BoardLevel0


class BeagleBoneBlack(BoardLevel0):

    def __init__(self):
        super(BeagleBoneBlack, self).__init__()

    def cleanup(self):
        pass

    def _set_pin_mode(self, pin, mode):
        pass

    def _set_pin_state(self, pin, state):
        pass
