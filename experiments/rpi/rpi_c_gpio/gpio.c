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
    int errno;
    int fd = open("/sys/class/gpio/export", O_WRONLY);

    if(fd < 0){
        printf("Fail export\n");
        return -1;
    }

    memset(buffer, 0, MAX_BUFFER);
    sprintf(buffer, "%d", gpio_id);
    errno = write(fd, buffer, strlen(buffer));

    if(errno){
        printf("Fail[errno %d]\n", errno);
        return -1;
    }

    close(fd);
    return 0;
}

DLLExport int disable_pin(int gpio_id) {

    char buffer[MAX_BUFFER];
    int errno;
    int fd = open("/sys/class/gpio/unexport", O_WRONLY);

    if(fd < 0){
        printf("Fail unexport\n");
        return -1;
    }

    memset(buffer, 0, MAX_BUFFER);
    sprintf(buffer, "%d", gpio_id);
    errno = write(fd, buffer, strlen(buffer));

    if(errno){
        printf("Fail[errno %d]\n", errno);
        return -1;
    }

    close(fd);
    return 0;
}

DLLExport int set_pin_direction(int gpio_id, char *direction) {

    int fd;
    int errno;
    char buffer[MAX_BUFFER];

    sprintf(buffer, "/sys/class/gpio/gpio%d/direction", gpio_id);
    fd = open(buffer, O_WRONLY);
    if(fd < 0){
        printf("Fail direction\n");
        return -1;
    }

    errno = write(fd, direction, strlen(direction));

    if(errno){
        printf("Fail[errno %d]\n", errno);
        return -1;
    }


    close(fd);

    return 0;
}

DLLExport int set_pin_value(int gpio_id, char *value) {

    int fd;
    int errno;
    char buffer[MAX_BUFFER];

    sprintf(buffer, "/sys/class/gpio/gpio%d/value", gpio_id);
    fd = open(buffer, O_WRONLY);

    if(fd < 0){
        printf("Fail value\n");
        return -1;
    }

    errno = write(fd, value, strlen(value));

    if(errno){
        printf("Fail[errno %d]\n", errno);
        return -1;
    }


    close(fd);
    return 0;
}

DLLExport int get_pin_value(int gpio_id) {

    int fd;
    int errno;
    char value;
    char buffer[MAX_BUFFER];

    sprintf(buffer, "/sys/class/gpio/gpio%d/value", gpio_id);
    fd = open(buffer, O_RDONLY);

    if(fd < 0){
        printf("Fail value\n");
        return -1;
    }

    errno = read(fd, &value, 1);

    if(errno){
        printf("Fail[errno %d]\n", errno);
        return -1;
    }


    close(fd);
    return value;
}

