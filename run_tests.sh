#!/bin/bash

#echo "Testing on GhostBoard..."
#python -m doctest pingo/ghost/tests/digital.rst $1
#echo "Testing on Target..."
#python pingo/test/test.py $1

if [ ! -d "test_output" ]; then
    mkdir test_output
fi

echo "RaspberryPi:"
sudo python pingo/rpi/tests/test.py 2> test_output/rpi.txt
tail -1 test_output/rpi.txt

echo "AutoDetect:"
python pingo/detect/tests/test.py 1>/dev/null 2> test_output/detect.txt
tail -1 test_output/detect.txt

echo "GhostBoard:"
python pingo/ghost/tests/test.py 1>/dev/null 2> test_output/ghost.txt
tail -1 test_output/ghost.txt

echo "BeagleBoneBlack:"
python pingo/bbb/tests/test.py 2> test_output/bbb.txt
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

