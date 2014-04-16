/*
* ADC test program for a10
*/
#include <core.h>
int adc_id = 0;
int delay_us = 100000;

void setup()
{
    if ( argc != 2 )
    {
        printf("Usage %s ADC_ID(0/1/2/3/4/5)\n", argv[0]);
        exit(-1);   
    }
    
   
    adc_id = atoi(argv[1]);
    
    printf("read adc value on ADC%d, delay is %d usecs\n",
        adc_id, delay_us);
}

void loop()
{
    int value = analogRead(adc_id); // get adc value

    printf("ADC%d level is %d\n",adc_id, value);

    delayMicroseconds(delay_us);  
}
