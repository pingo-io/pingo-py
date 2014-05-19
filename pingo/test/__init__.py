import level0
import level1


def not_has_module(module_name):
    try:
        __import__(module_name)
        return False
    except ImportError:
        return True
