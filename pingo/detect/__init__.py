from detect import get_board


def has_module(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False


def check_board(pingo_board):
    current = get_board()
    return isinstance(current, pingo_board)
