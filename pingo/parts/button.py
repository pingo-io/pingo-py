import time
import threading


class Switch(object):
    """Button like component with two stable states"""

    def __init__(self, pin):
        """
        :param pin: A instance of DigitalPin
        """
        self.pin = pin
        self.pin.mode = 'IN'
        self.polling_task = None
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
        if self.polling_task is not None:
            if self.polling_task.active:
                self.polling_task.terminate()
                self.polling_task = None

    def start(self):
        if self.polling_task is not None:
            if self.polling_task.active:
                self.stop()
        self.polling_task = PollingTask(self)
        threading.Thread(target=self.polling_task.run).start()


class PollingTask(object):
    def __init__(self, switch):
        """
        :param switch: Switch instance to poll
        """
        self.switch = switch
        self.active = False

    def terminate(self):
        self.active = False

    def run(self):
        self.active = True
        last_state = self.switch.pin.state
        while self.active:
            current_state = self.switch.pin.state
            if current_state != last_state:
                if current_state == 'HIGH':
                    last_state = current_state
                    self.switch._up_callback()
                elif current_state == 'LOW':
                    last_state = current_state
                    self.switch._down_callback()
            time.sleep(0.05)
