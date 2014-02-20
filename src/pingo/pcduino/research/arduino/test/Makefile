LIBS=-L../../sample/core -larduino -lspi
INCS=-I../../sample/core/include
TARGET=../../sample/test

OBJS = io_test adc_test pwm_test spi_test adxl345_test

all: $(OBJS)
	@mkdir -p $(TARGET)
	@mv $(OBJS) $(TARGET)

io_test: io_test.c
	$(CC) $(LIBS) $(INCS) $< -o $@

adc_test: adc_test.c
	$(CC) $(LIBS) $(INCS) $< -o $@

pwm_test: pwm_test.c
	$(CC) $(LIBS) $(INCS) $< -o $@

spi_test: spi_test.c  
	$(CC) $(LIBS) $(INCS) $< -o $@

adxl345_test: adxl345_test.c
	$(CC) $< -o $@
clean:
	@for i in $(OBJS); do rm -f $(TARGET)/$$i; done
