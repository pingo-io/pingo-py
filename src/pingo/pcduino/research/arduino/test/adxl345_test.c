#ifndef ADXL345_h
#define ADXL345_h

/* ------- Register names ------- */
#define ADXL345_DEVID 0x00
#define ADXL345_RESERVED1 0x01
#define ADXL345_THRESH_TAP 0x1d
#define ADXL345_OFSX 0x1e
#define ADXL345_OFSY 0x1f
#define ADXL345_OFSZ 0x20
#define ADXL345_DUR 0x21
#define ADXL345_LATENT 0x22
#define ADXL345_WINDOW 0x23
#define ADXL345_THRESH_ACT 0x24
#define ADXL345_THRESH_INACT 0x25
#define ADXL345_TIME_INACT 0x26
#define ADXL345_ACT_INACT_CTL 0x27
#define ADXL345_THRESH_FF 0x28
#define ADXL345_TIME_FF 0x29
#define ADXL345_TAP_AXES 0x2a
#define ADXL345_ACT_TAP_STATUS 0x2b
#define ADXL345_BW_RATE 0x2c
#define ADXL345_POWER_CTL 0x2d
#define ADXL345_INT_ENABLE 0x2e
#define ADXL345_INT_MAP 0x2f
#define ADXL345_INT_SOURCE 0x30
#define ADXL345_DATA_FORMAT 0x31
#define ADXL345_DATAX0 0x32
#define ADXL345_DATAX1 0x33
#define ADXL345_DATAY0 0x34
#define ADXL345_DATAY1 0x35
#define ADXL345_DATAZ0 0x36
#define ADXL345_DATAZ1 0x37
#define ADXL345_FIFO_CTL 0x38
#define ADXL345_FIFO_STATUS 0x39

#define ADXL345_BW_1600 0xF // 1111
#define ADXL345_BW_800  0xE // 1110
#define ADXL345_BW_400  0xD // 1101  
#define ADXL345_BW_200  0xC // 1100
#define ADXL345_BW_100  0xB // 1011  
#define ADXL345_BW_50   0xA // 1010 
#define ADXL345_BW_25   0x9 // 1001 
#define ADXL345_BW_12   0x8 // 1000 
#define ADXL345_BW_6    0x7 // 0111
#define ADXL345_BW_3    0x6 // 0110


/* 
 Interrupt PINs
 INT1: 0
 INT2: 1
 */
#define ADXL345_INT1_PIN 0x00
#define ADXL345_INT2_PIN 0x01

/* 
 Interrupt bit position
 */
#define ADXL345_INT_DATA_READY_BIT 0x07
#define ADXL345_INT_SINGLE_TAP_BIT 0x06
#define ADXL345_INT_DOUBLE_TAP_BIT 0x05
#define ADXL345_INT_ACTIVITY_BIT   0x04
#define ADXL345_INT_INACTIVITY_BIT 0x03
#define ADXL345_INT_FREE_FALL_BIT  0x02
#define ADXL345_INT_WATERMARK_BIT  0x01
#define ADXL345_INT_OVERRUNY_BIT   0x00

#define ADXL345_DATA_READY 0x07
#define ADXL345_SINGLE_TAP 0x06
#define ADXL345_DOUBLE_TAP 0x05
#define ADXL345_ACTIVITY   0x04
#define ADXL345_INACTIVITY 0x03
#define ADXL345_FREE_FALL  0x02
#define ADXL345_WATERMARK  0x01
#define ADXL345_OVERRUNY   0x00

#endif

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#define I2C_SET_CMD "../core/i2cset -y 2 0x53"
#define I2C_GET_CMD "../core/i2cget -y 2 0x53"
static void write8(int reg, unsigned char value)
{
	char cmd[1024];
	memset((void *)&cmd, 0, sizeof(cmd));
	sprintf(cmd, "%s 0x%.2x 0x%.2x 2>/dev/null", I2C_SET_CMD, reg, value);
	system(cmd);
}

static unsigned char read8(int reg)
{
	char cmd[1024];
	char value[10];
	FILE *fp = NULL;
	memset(cmd, 0, sizeof(cmd));
	memset(value, 0, sizeof(value));
	sprintf(cmd, "%s 0x%.2x 2>/dev/null", I2C_GET_CMD, reg);
	fp = popen(cmd, "r");
	fread(value, 1 ,sizeof(value), fp);
	fclose(fp);
	return atoi((char *)value+2);
}

static unsigned short read16(int reg)
{
	char cmd[1024];
	char value[10];
	int ret = 0;
	FILE *fp = NULL;
	memset(cmd, 0, sizeof(cmd));
	memset(value, 0, sizeof(value));
	sprintf(cmd, "%s 0x%.2x w 2>/dev/null", I2C_GET_CMD, reg);
	fp = popen(cmd, "r");
	ret = fread(value, 1 ,sizeof(value), fp);
	fclose(fp);
	return atoi((char *)value+2);
}


void readXYZ(void)
{
	unsigned short x, y, z;
	x = read16(ADXL345_DATAX0);
	y = read16(ADXL345_DATAY0);
	z = read16(ADXL345_DATAZ0);

	printf("x=%d, y=%d, z=%d\n", x, y, z);	
}

void setRegisterBit(int reg, char bit, char high)
{
	int value = read8(reg);
//value =  i2cget -y 2 0x53 reg
	if (high )
		value |= (1<<bit);
	else
		value &= ~(1<<bit);
	write8(reg, value);
}
void setup()
{
	//powerOn();
	write8(ADXL345_POWER_CTL, 0);
	write8(ADXL345_POWER_CTL, 16);
	write8(ADXL345_POWER_CTL, 8); 

	//set activity/ inactivity thresholds (0-255)
	write8(ADXL345_THRESH_ACT, 75); //setActivityThreshold(75); //62.5mg per increment	
	write8(ADXL345_THRESH_INACT, 75);//setInactivityThreshold(75); //62.5mg per increment
	write8(ADXL345_TIME_INACT, 10); //setTimeInactivity(10); // how many seconds of no activity is inactive?
	
	//look of activity movement on this axes - 1 == on; 0 == off 
	setRegisterBit(ADXL345_ACT_INACT_CTL, 6, 1);//setActivityX(1);
	setRegisterBit(ADXL345_ACT_INACT_CTL, 5, 1);//setActivityY(1);
	setRegisterBit(ADXL345_ACT_INACT_CTL, 4, 1); //setActivityZ(1);
	
	//look of inactivity movement on this axes - 1 == on; 0 == off
	setRegisterBit(ADXL345_ACT_INACT_CTL, 2, 1);//setInactivityX(1);
	setRegisterBit(ADXL345_ACT_INACT_CTL, 1, 1);//setInactivityY(1);
	setRegisterBit(ADXL345_ACT_INACT_CTL, 0, 1);//setInactivityZ(1);
	
	//look of tap movement on this axes - 1 == on; 0 == off
	setRegisterBit(ADXL345_TAP_AXES, 2, 0);//setTapDetectionOnX(0);
	setRegisterBit(ADXL345_TAP_AXES, 1, 0);//setTapDetectionOnY(0);
	setRegisterBit(ADXL345_TAP_AXES, 0, 1);//setTapDetectionOnZ(1);
	
	//set values for what is a tap, and what is a double tap (0-255)
	write8(ADXL345_THRESH_TAP, 50);//setTapThreshold(50); //62.5mg per increment
	write8(ADXL345_DUR, 15);//setTapDuration(15); //625¦Ìs per increment
	write8(ADXL345_LATENT, 80); //setDoubleTapLatency(80); //1.25ms per increment
	write8(ADXL345_WINDOW, 200); //setDoubleTapWindow(200); //1.25ms per increment
	
	//set values for what is considered freefall (0-255)
	write8(ADXL345_THRESH_FF, 7); //setFreeFallThreshold(7); //(5 - 9) recommended - 62.5mg per increment
	write8(ADXL345_TIME_FF, 45); //setFreeFallDuration(45); //(20 - 70) recommended - 5ms per increment
}

int main(int argc, char **argv)
{
	system("sudo chmod 777 /dev/i2c-* 2>/dev/null");
	setup();
	while(1)
	{
		readXYZ();
		usleep(200000);
		
	}
	return 0;
}

