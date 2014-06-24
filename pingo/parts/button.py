import time
import threading

class Switch(threading.Thread):
    """ Button like component with two stable states """
    def __init__(self, pin):
        super(Switch, self).__init__()
        self.setDaemon(True)
        self.pin = pin
        self.pin.mode = 'IN'
        self._flag = threading.Event()
        self._up_callback = lambda: None
        self._down_callback = lambda: None

    def set_callback_up(self, callback, *args, **kwargs):
        def callback_wrapper():
            return callback(*args, **kwargs)
        self._up_callback = callback_wrapper

    def set_callback_down(self, callback, *args, **kwargs):
        def callback_wrapper():
            return callback(*args, **kwargs)
        self._down_callback = callback_wrapper

    def stop(self):
        self._flag.clear()
        self.join()

    def run(self):
        self._flag.set()
        last_state = self.pin.state
        while self._flag.is_set():
            current_state = self.pin.state
            if current_state != last_state:
                if current_state == 'HIGH':
                    last_state = current_state
                    self._up_callback()
                elif current_state == 'LOW':
                    last_state = current_state
                    self._down_callback()
            time.sleep(0.05)
