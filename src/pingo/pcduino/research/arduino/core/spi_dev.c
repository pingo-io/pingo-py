#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/spi/spidev.h>
#include <core.h>
#include "spi_dev.h"

int fd=0;
static const char *device = "/dev/spidev0.0";
static int mode;
static int bits = 8;
static int speed = 500000;
static unsigned short delay_usecs = 0;

void spi_begin();
void spi_end();
void spi_setBitOrder(int bitOrder);
void spi_setDataMode(int mode);
void spi_setClockDivider(int rate_div);
char spi_transfer(char val, int transferMode);

struct SPIDev SPI = {
        .begin = spi_begin,
        .end = spi_end,
        .setBitOrder = spi_setBitOrder,
        .setDataMode = spi_setDataMode,
        .setClockDivider = spi_setClockDivider,
        .transfer = spi_transfer
};

static void pabort(const char *s)
{
    perror(s);
    abort();
}

void spi_begin() 
{
    int ret =0;
    int max_speed = 0, default_mode=0;
    
    pinMode(10, 2); //CS
    pinMode(11, 2); //MOSI
    pinMode(12, 2); //MISO
    pinMode(13, 2); //CLK
		
    if (!fd)
   	fd = open(device, O_RDWR);
    if (fd < 0)
        pabort("can't open device");

    ret = ioctl(fd, SPI_IOC_RD_MODE, &default_mode);
    if (ret == -1)
        pabort("can't get spi mode");
    mode = default_mode;

    ret = ioctl(fd, SPI_IOC_RD_MAX_SPEED_HZ, &max_speed);
    if (ret == -1)
        pabort("can't get max speed hz");
    speed = max_speed;

    printf("spi mode: 0x%x\n", mode);
    printf("bits per word: %d\n", bits);
    printf("max speed: %d Hz (%d KHz)\n", speed, speed/1000);

}

void spi_end() 
{
    if (fd) 
        close(fd);    
}

void spi_setBitOrder(int bitOrder)
{
   int order = 0, ret = 0;
    /*
     * bits per word
     */
    if(bitOrder == LSBFIRST) 
        order = 1;
    else if(bitOrder == MSBFIRST) 
        order = 0;    

    ret = ioctl(fd, SPI_IOC_WR_LSB_FIRST, &order);
    if (ret == -1)
        pabort("can't set bits order");

}

void spi_setDataMode(int mode)
{
    int ret = 0;
    /*
     * spi mode
     */
    ret = ioctl(fd, SPI_IOC_WR_MODE, &mode);
    if (ret == -1)
        pabort("can't set spi mode");

}

void spi_setClockDivider(int rate_div)
{
    switch (rate_div)
    {
        case SPI_CLOCK_DIV1:
            break;
        case SPI_CLOCK_DIV2:
            speed = speed/2;
            break;
        case SPI_CLOCK_DIV4:
            speed = speed/4;
            break;
        case SPI_CLOCK_DIV8:
            speed = speed/8;
            break;
        case SPI_CLOCK_DIV16:
            speed = speed/16;
            break;
        case SPI_CLOCK_DIV32:
            speed = speed/32;
            break;
        case SPI_CLOCK_DIV64:
            speed = speed/64;
            break;
        case SPI_CLOCK_DIV128:
            speed = speed/128;
            break;

        default:
            break;
    }
}

char spi_transfer(char val, int transferMode)
{
    int ret=0;
    char tx = val;
    char rx = 0;
    struct spi_ioc_transfer tr[2]={0};

    if (transferMode == SPI_CONTINUE) 
	   delay_usecs = 0;
	else if (transferMode == SPI_LAST)  
	   delay_usecs = 0xAA55;	

	memset(tr, 0x0, sizeof(tr));
	tr[0].tx_buf = (unsigned long)&tx;
	tr[0].len = 1;
	tr[0].speed_hz = speed;
	tr[0].bits_per_word = bits;
	tr[0].delay_usecs = delay_usecs;
	tr[1].rx_buf = (unsigned long)&rx;
	tr[1].len = 1;
	tr[1].speed_hz = speed;
	tr[1].bits_per_word = bits;
	tr[1].delay_usecs = delay_usecs;

    ret = ioctl(fd, SPI_IOC_MESSAGE(2), tr);
    if (ret < 1)
        pabort("can't send spi message");

    //printf("rx = %.2X \r\n", rx);

    return rx;
}
