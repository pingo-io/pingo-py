/*
* PWM test program for a10
*/
#include <core.h>
int pwm_id = 0;
int delay1_us = 200000;
int delay2_us = 1000000;

void setup()
{
    if ( argc != 2 )
    {
        printf("Usage %s PWM_ID(0-5)\n", argv[0]);
        exit(-1);   
    }
    
   
    pwm_id = atoi(argv[1]);
    
    printf("PWM%d test\n", pwm_id);
}

void loop()
{
    int value = MAX_PWM_LEVEL/2;
    analogWrite(pwm_id, value);
    delayMicroseconds(delay1_us); 
    analogWrite(pwm_id, 0); // turn off
    delayMicroseconds(delay2_us);
}

