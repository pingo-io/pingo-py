#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <fcntl.h>

#include "gpio.h"

#define LINUX
#ifdef LINUX
    #define DLLImport
    #define DLLExport 
#else
    #define DLLImport __declspec(dllimport)
    #define DLLExport __declspec(dllexport)
#endif

#define MAX_BUFFER 128

/*
http://falsinsoft.blogspot.com.br/2012/11/access-gpio-from-linux-user-space.html
*/

DLLExport int enable_pin(int gpio_id) {

    char buffer[MAX_BUFFER];
    int fd = open("/sys/class/gpio/export", O_WRONLY);

    if(fd < 0) return 1;
    memset(buffer, 0, MAX_BUFFER);

    sprintf(buffer, "%d", gpio_id); 
    write(fd, buffer, strlen(buffer));

    close(fd);    
    return 0;
}

DLLExport int disable_pin(int gpio_id) {

    char buffer[MAX_BUFFER]; 
    int fd = open("/sys/class/gpio/unexport", O_WRONLY); 
    
    if(fd < 0) return 1;
    memset(buffer, 0, MAX_BUFFER);

    sprintf(buffer, "%d", gpio_id); 
    write(fd, buffer, strlen(buffer));

    close(fd);
    return 0;
}

DLLExport int set_pin_direction(int gpio_id, char *direction) {

    int fd; 
    char buffer[MAX_BUFFER]; 

    sprintf(buffer, "/sys/class/gpio/gpio%d/direction", gpio_id);
    fd = open(buffer, O_WRONLY);
    if(fd < 0) return 1;

    write(fd, direction, strlen(direction)); 
    close(fd);

    return 0;
}

DLLExport int set_pin_value(int gpio_id, char *value) {

    int fd; 
    char buffer[MAX_BUFFER]; 

    sprintf(buffer, "/sys/class/gpio/gpio%d/direction", gpio_id);
    fd = open(buffer, O_WRONLY);

    if(fd < 0) return 1;
    write(fd, value, strlen(value)); 

    close(fd);
    return 0;
}

DLLExport int get_pin_value(int gpio_id) {

    int fd;
    char value;
    char buffer[MAX_BUFFER];

    sprintf(buffer, "/sys/class/gpio/gpio%d/direction", gpio_id);
    fd = open(buffer, O_RDONLY);

    if(fd < 0) return 1;
    read(fd, &value, 1); 

    close(fd);
    return value;
}

