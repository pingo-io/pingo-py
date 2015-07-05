"""
Copied from:
https://github.com/tino/pyFirmata/blob/master/pyfirmata/util.py
"""


def pin_list_to_board_dict(capability_query_response):
    """
    Capability Response codes:
        INPUT:  0, 1
        OUTPUT: 1, 1
        ANALOG: 2, 10
        PWM:    3, 8
        SERV0:  4, 14
        I2C:    6, 1
    """

    board_dict = {
        'digital': [],
        'analog': [],
        'pwm': [],
        'servo': [],
        'i2c': [],
        'disabled': [],
    }

    # i split pins of list:
    pin_list = [[]]
    for b in capability_query_response:
        if b == 127:
            pin_list.append([])
        else:
            pin_list[-1].append(b)

    # Finds the capability of each pin
    for i, pin in enumerate(pin_list):
        if not pin:
            board_dict['disabled'] += [i]
            board_dict['digital'] += [i]
            continue

        for j, _ in enumerate(pin):
            # Iterate over evens
            if j % 2 == 0:
                # This is safe. try: range(10)[5:50]
                if pin[j:j + 4] == [0, 1, 1, 1]:
                    board_dict['digital'] += [i]

                if pin[j:j + 2] == [2, 10]:
                    board_dict['analog'] += [i]

                if pin[j:j + 2] == [3, 8]:
                    board_dict['pwm'] += [i]

                if pin[j:j + 2] == [4, 14]:
                    board_dict['servo'] += [i]

                if pin[j:j + 2] == [6, 1]:
                    board_dict['i2c'] += [i]

    # We have to deal with analog pins:
    # - (14, 15, 16, 17, 18, 19)
    # + (0, 1, 2, 3, 4, 5)
    diff = set(board_dict['digital']) - set(board_dict['analog'])
    board_dict['analog'] = [n for n, _ in enumerate(board_dict['analog'])]

    # Digital pin problems:
    # - (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    # + (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    board_dict['digital'] = [n for n, _ in enumerate(diff)]
    # Based on lib Arduino 0017
    board_dict['servo'] = board_dict['digital']

    # Turn lists into tuples
    # Using dict for Python 2.6 compatibility
    board_dict = dict([
        (key, tuple(value))
        for key, value
        in board_dict.items()
    ])

    return board_dict
