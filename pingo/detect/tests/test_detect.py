import os
import sys
import time
import unittest

import pytest

import pingo


class DetectBasics(unittest.TestCase):

    def test_board(self):
        board = pingo.detect.MyBoard()
        assert isinstance(board, pingo.Board)

if __name__ == '__main__':
    unittest.main()
