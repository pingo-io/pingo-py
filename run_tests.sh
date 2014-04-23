#!/bin/bash

#echo "Testing on GhostBoard..."
#python -m doctest pingo/ghost/tests/digital.rst $1
#echo "Testing on Target..."
#python pingo/test/test.py $1

mkdir test_output

echo "GhostBoard:"
python pingo/ghost/tests/test.py 2> test_output/ghost.txt
tail -1 test_output/ghost.txt

echo "RaspberryPi:"
python pingo/rpi/tests/test.py 2> test_output/rpi.txt
tail -1 test_output/rpi.txt

echo "BeagleBoneBlack:"
python pingo/bbb/tests/bbb.py 2> test_output/bbb.txt
tail -1 test_output/bbb.txt

echo "ArduinoFirmata:"
python pingo/arduino/tests/test.py 2> test_output/arduino.txt
tail -1 test_output/arduino.txt

echo "Udoo:"
python pingo/udoo/tests/test.py 2> test_output/udoo.txt
tail -1 test_output/udoo.txt

echo "PcDuino:"
python pingo/pcduino/tests/test.py 2> test_output/pcduino.txt
tail -1 test_output/pcduino.txt
