TARGET = fsgpio.so
LIBS = -lm
CC = gcc
CFLAGS = -shared -g -Wall -fPIC
INCLUDE = -I/usr/include/python2.7

.PHONY: clean all default

default: $(TARGET)
all: default

OBJECTS = $(patsubst %.c, %.o, $(wildcard *.c))
HEADERS = $(wildcard *.h)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

.PRECIOUS: $(TARGET) $(OBJECTS)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -shared -Wall $(INCLUDE) $(LIBS) -o $@

clean:
	-rm -f *.o
	-rm -f $(TARGET)
