import os
import sys
import time

import pytest

import pingo


class DetectBasics():

    def test_board(self):
        board = pingo.detect.MyBoard()
        assert isinstance(board, pingo.Board)
