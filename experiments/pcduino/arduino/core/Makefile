TARGET=../../sample/core
INCS=-I ./include/

all:
	@mkdir -p $(TARGET)/include
	$(CC) $(INCS) core.c -c -fPIC -shared -o $(TARGET)/libarduino.so
	$(CC) $(INCS) core.c -c -fPIC -static -o $(TARGET)/libarduino.a

	$(CC) $(INCS) spi_dev.c -c -fPIC -shared -o $(TARGET)/libspi.so
	$(CC) $(INCS) spi_dev.c -c -fPIC -static -o $(TARGET)/libspi.a
	@cp include/core.h $(TARGET)/include/
	@cp include/spi_dev.h $(TARGET)/include/

clean:
	@rm -rf $(TARGET)/include
	@rm -f $(TARGET)/*.so
	@rm -f $(TARGET)/*.a
