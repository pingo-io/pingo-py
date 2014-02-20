#ifndef _SPI_H_INCLUDED
#define _SPI_H_INCLUDED

#include <linux/types.h>

#define LSBFIRST 0
#define MSBFIRST 1

#define SPI_CONTINUE 0
#define SPI_LAST     1

#define SPI_MODE0 0x00
#define SPI_MODE1 0x01
#define SPI_MODE2 0x02
#define SPI_MODE3 0x03

#define SPI_CLOCK_DIV1   0x00
#define SPI_CLOCK_DIV2   0x01
#define SPI_CLOCK_DIV4   0x02
#define SPI_CLOCK_DIV8   0x03
#define SPI_CLOCK_DIV16  0x04
#define SPI_CLOCK_DIV32  0x05
#define SPI_CLOCK_DIV64  0x06
#define SPI_CLOCK_DIV128 0x07


struct SPIDev {
   void (*begin)(void);
   void (*end)(void);
   void (*setBitOrder)(int bitOrder);
   void (*setDataMode)(int mode);
   void (*setClockDivider)(int rate_div);
   char (*transfer)(char val, int transferMode);

};

extern struct SPIDev SPI;

#endif
