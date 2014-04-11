import ctypes

dll = ctypes.cdll.LoadLibrary("./fsgpio.so");
dll.enable_pin(4);
dll.set_pin_direction(4, "out");
dll.set_pin_value(4, "1");
r = dll.get_pin_value(4)
dll.disable_pin(4);

print r

