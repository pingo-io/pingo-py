import os
import sys
import unittest
import time

import pingo


class DetectBasics(unittest.TestCase):

    def test_board(self):
        board = pingo.detect.MyBoard()
        self.assertIsInstance(board, pingo.Board)


if __name__ == '__main__':
    unittest.main()

