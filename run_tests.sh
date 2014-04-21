#!/bin/bash
echo "Testing on GhostBoard..."
python -m doctest pingo/ghost/tests/digital.rst $1
echo "Testing on Target..."
python pingo/test/test.py $1
