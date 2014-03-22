Arduino API 
===========================================================
0. time
void delay(unsigned long ms);
void delayMicroseconds(unsigned int us);

1. digital I/O
void pinMode(int pin, unsigned int mode);
void digitalWrite(int pin, int value);
int digitalRead(int pin);

2. ADC
int analogRead(int pin);

3. PWM
void analogWrite(int pin, int value); 

4. SPI
begin() 
end() 
setBitOrder() 
setClockDivider() 
setDataMode() 
transfer() 

5. I2C

6. UART

