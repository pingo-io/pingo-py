#!/bin/env python

# DESCRIPTION : This sketch is written in Python and allows you to control Sitara's gpios
# To make the script executable type this command in terminal: $ chmod +x PinControl.py
# To execute the script use : $ sudo ./PinControl.py
# then follow the instructions that appear in the terminal

import sys

num = 0
GPIO_DIR = "/sys/class/gpio"

gpio_map = {
  104: 32,
  105: 33,
  106: 34,
  107: 35,
  108: 36,
  109: 37,
  110: 38,
  111: 39,
  112: 64,
  113: 68,
  114: 67,
  115: 66,
  116: 26,
  117: 114,
  118: 115,
  119: 116,
  120: 62,
  121: 63,
  122: 44,
  123: 45,
  124: 46,
  125: 47,
  126: 19,
  127: 20,
}

while True:
  print
  print "INSTRUCTIONS:"
  print "type 'start' to control an Arduino Tre's pin"
  print "type 'exit' to quit the script"

  # read the command you type in input
  cmd = raw_input('> ')
  if cmd.lower() == "exit":  # if you type "exit" the script quits
    print "End of the script"
    sys.exit(1)

  elif cmd.lower() == "start":  # type start to start the script and control a gpio

    print "type the pin number"
    # num is the gpio number instead n is the gpio's number in filesystem
    num = raw_input('> ')
    try:
      num = int(num)
    except ValueError:
      num = 0
    if num in gpio_map:
        print "digital pin is : PIN", num
    else:
      print "Pin's number is wrong"
      print "Arduino Tre has 28 digital pin."
      print "A pin number must be a number between 104 and 127"
      print "End of the script"
      sys.exit(2)

    print "Choose the pin's mode (INPUT or OUTPUT):"
    mode = raw_input('> ')

    # set the mode of gpio
    if mode.lower().startswith('out'):
        print "out" >> "$GPIO_DIR/gpio$n/direction"
        print "Pin $num sets as OUTPUT"

    elif [[ ("$mode" == "in") || ("$mode" == "INPUT") ]]; then
        print "in" >> "$GPIO_DIR/gpio$n/direction"
        print "Pin $num sets as INPUT"

        value=$(cat $GPIO_DIR/gpio$n/value)
        print "Value of pin $num : $value"
        exit

    else print "Pin's mode is wrong"
         print "Pin's mode can be INPUT (in) or OUTPUT (out)"
         print "End of the script"
         exit 2
    fi

    print
    print "type the pin's state (HIGH or LOW)"
    print -n "> "

    # set the state of a gpio
    read state
    if [[ ($state = 1) || ("$state" == "HIGH") ]]; then
        if [[ ("$mode" == "in") || ("$mode" == "INPUT") ]]; then
            print "It's impossible to set on HIGH a pin declared as INPUT"
            print "End of the script"
            exit
        else
            print "1" >> "$GPIO_DIR/gpio$n/value"
            print "Pin $num sets on HIGH"
        fi

    elif [[ ($state = 0) || ("$state" == "LOW") ]]; then
        print "0" >> "$GPIO_DIR/gpio$n/value"
        print "Pin $num sets on LOW"

    else print "Pin's state is wrong"
         print "Pin's state can be HIGH (1) or LOW (0)"
         exit 2
    fi

  else print
       print "Command is wrong. End of the script"
       exit 2
  fi

done
