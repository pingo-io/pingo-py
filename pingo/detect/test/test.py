import os
import sys
import unittest
import time

sys.path.append("../../..")

import pingo


class DetectBasics():

    def test_board(self):
        board = pingo.detect.MyBoard()
        self.assertIsInstance(board, pingo.Board)


if __name__ == '__main__':
    unittest.main()

