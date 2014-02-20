/*
* I/O test program for a10
*/
#include <core.h>
int led_pin = 1;
int btn_pin = 5;

void setup()
{
    if ( argc != 3 )
    {
        printf("Usage %s BUTTON_PIN_NUM(0-13) LED_PIN_NUM(0-13)\n", argv[0]);
        exit(-1);   
    }
    
   
    btn_pin = atoi(argv[1]);
    led_pin = atoi(argv[2]);
    
    printf("press button (connected to pin %d) to turn on LED (connected to pin %d)\n",
        btn_pin, led_pin);
            
    pinMode(led_pin, OUTPUT);
    pinMode(btn_pin, INPUT);
}

void loop()
{
    int value = digitalRead(btn_pin); // get button status

    if ( value == HIGH )  // button pressed
    {
        digitalWrite(led_pin, HIGH); // turn on LED
    }
    else // button released
    {
        digitalWrite(led_pin, LOW); // turn off LED
    }
    delay(100);  
}
