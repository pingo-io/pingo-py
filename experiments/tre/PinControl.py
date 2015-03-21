#!/bin/bash

# DESCRIPTION : This sketch is written in bash and it allows to control Sitara's gpios
# To make executable the script digit in terminal this command : $ chmod +x PinControl.sh
# To execute the script use : $ ./PinControl.sh
# then follow the instuctions that appear in the terminal

num=0
GPIO_DIR="/sys/class/gpio"

while true; do
  echo
  echo "INSTRUCTIONS :"
  echo "Digit 'start' to control an Arduino Tre's pin"
  echo "Digit 'exit' to quit the script"
  echo -n "> "
  
  # read the command you digit in input
  read cmd   
  if [ "$cmd" == "exit" ]; then  # if you digit "exit" the script quits
    echo "End of the script"
    exit

  elif [ "$cmd" == "start" ]; then   # digit start to start the script and control a gpio
    
    echo
    echo "Digit the pin number"
    echo -n "> "

    read num    # num is the gpio number instead n is the gpio's number in filesystem
    if [[ "$num" -gt "103" && "$num" -lt "128" ]]; then
        echo "Digital pin is : PIN $num"
                                         
        if   [ $num = 104 ]; then n=32  
        elif [ $num = 105 ]; then n=33
        elif [ $num = 106 ]; then n=34
        elif [ $num = 107 ]; then n=35
        elif [ $num = 108 ]; then n=36
        elif [ $num = 109 ]; then n=37
        elif [ $num = 110 ]; then n=38
        elif [ $num = 111 ]; then n=39
        elif [ $num = 112 ]; then n=64
        elif [ $num = 113 ]; then n=68
        elif [ $num = 114 ]; then n=67
        elif [ $num = 115 ]; then n=66
        elif [ $num = 116 ]; then n=26
        elif [ $num = 117 ]; then n=114
        elif [ $num = 118 ]; then n=115
        elif [ $num = 119 ]; then n=116
        elif [ $num = 120 ]; then n=62
        elif [ $num = 121 ]; then n=63
        elif [ $num = 122 ]; then n=44
        elif [ $num = 123 ]; then n=45
        elif [ $num = 124 ]; then n=46
        elif [ $num = 125 ]; then n=47
        elif [ $num = 126 ]; then n=19
        elif [ $num = 127 ]; then n=20
        
        fi
    
    else echo "Pin's number is wrong"
         echo "Arduino Tre has 28 digital pin." 
         echo "A pin number must be a number between 100 and 127"
         echo "End of the script"
         exit 2
    fi

    echo
    echo "Choise the pin's mode (INPUT or OUTPUT) :"
    echo -n "> "
    
    # set the mode of gpio
    read mode 
    if [[ ("$mode" == "out") || ("$mode" == "OUTPUT") ]]; then
        echo "out" >> "$GPIO_DIR/gpio$n/direction"
        echo "Pin $num sets as OUTPUT"

    elif [[ ("$mode" == "in") || ("$mode" == "INPUT") ]]; then
        echo "in" >> "$GPIO_DIR/gpio$n/direction"
        echo "Pin $num sets as INPUT"

        value=$(cat $GPIO_DIR/gpio$n/value)
        echo "Value of pin $num : $value"
        exit

    else echo "Pin's mode is wrong"
         echo "Pin's mode can be INPUT (in) or OUTPUT (in)"
         echo "End of the script"
         exit 2
    fi

    echo
    echo "Digit the pin's state (HIGH or LOW)"
    echo -n "> "
    
    # set the state of a gpio
    read state
    if [[ ($state = 1) || ("$state" == "HIGH") ]]; then
        if [[ ("$mode" == "in") || ("$mode" == "INPUT") ]]; then
            echo "It's impossible to set on HIGH a pin declared as INPUT"
            echo "End of the script"
            exit
        else 
            echo "1" >> "$GPIO_DIR/gpio$n/value"
            echo "Pin $num sets on HIGH"
        fi

    elif [[ ($state = 0) || ("$state" == "LOW") ]]; then
        echo "0" >> "$GPIO_DIR/gpio$n/value"
        echo "Pin $num sets on LOW"

    else echo "Pin's state is wrong"
         echo "Pin's state can be HIGH (1) or LOW (0)"
         exit 2
    fi

  else echo
       echo "Command is wrong. End of the script"
       exit 2
  fi

done
