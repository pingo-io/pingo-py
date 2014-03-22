/*
* Arduino lib for a10
*/
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#include <a10.h>
#include <core.h>

void pinMode(int pin, unsigned int mode)
{
    char cmd[128];

    if ( (pin >= 0 && pin <=  MAX_GPIO_NUM) && (mode <= MAX_GPIO_MODE_NUM) )
    {
        memset((void *)cmd, 0, sizeof(cmd));
        sprintf(cmd, "echo %d > %s%s%d", 
            mode, GPIO_MODE_DIR, GPIO_IF_PREFIX, pin);
        system(cmd);
    }
    else
    {
        fprintf(stderr, "%s ERROR: invalid pin or mode, pin=%d, mode=%d\n",
            __FUNCTION__, pin, mode);
        exit(-1);
     }
}

void digitalWrite(int pin, int value)
{
    char cmd[128];

    if ( (pin >= 0 && pin <=  MAX_GPIO_NUM) && (value == HIGH || value == LOW) )
    {
        memset((void *)cmd, 0, sizeof(cmd));
        sprintf(cmd, "echo %d > %s%s%d", 
            value, GPIO_PIN_DIR, GPIO_IF_PREFIX, pin);
        system(cmd);
    }
    else
    {
        fprintf(stderr, "%s ERROR: invalid pin or mode, pin=%d, value=%d\n",
            __FUNCTION__, pin, value);
        exit(-1);
     }    
}

int digitalRead(int pin)
{
    char path[128];
    char buf[128];    
    int ret = -1;
    int fd = -1;     
        
    if ( pin >= 0 && pin <= MAX_GPIO_NUM )
    {
        memset((void *)path, 0, sizeof(path));
        sprintf(path, "%s%s%d", GPIO_PIN_DIR, GPIO_IF_PREFIX, pin);
        fd = open(path, O_RDONLY);
        if ( fd < 0 )
        {
            fprintf(stderr, "open %s failed\n", path);
            exit(-1);
        }
        
        ret = read(fd, buf, sizeof(buf));
        
        if ( ret <= 0 )
        {
            fprintf(stderr, "read %s failed\n", path);
            close(fd);
            exit(-1);
        }
        
        ret = buf[0] - '0';
        switch( ret )
        {
            case LOW:
            case HIGH:
                break;
            default:
                ret = -1;
                break;
        }
    }
    else
    {
        fprintf(stderr, "%s ERROR: invalid pin, pin=%d\n", __FUNCTION__, pin);
        exit(-1);
    }      
    return ret;
}

void delay(unsigned long ms)
{
    usleep(ms*1000);
}

void delayMicroseconds(unsigned int us)
{
    usleep(us);
}

int analogRead(int pin)
{
    char str[10];
    char buf[128];    
    int ret = -1;
    int fd = -1;
    char *p = NULL;
        
    if ( pin >= 0 && pin <= MAX_ADC_NUM )
    {
        memset((void *)str, 0, sizeof(str));
        strcpy(str,ADC_IF);
        sprintf(str, "%s%d",str, pin);
        fd = open(str, O_RDONLY);
        if ( fd < 0 )
        {
            fprintf(stderr, "open %s failed\n", str);
            exit(-1);
        }
        
        ret = read(fd, buf, sizeof(buf));
        
        if ( ret <= 0 )
        {
            fprintf(stderr, "read %s failed\n", str);
            close(fd);
            exit(-1);
        }

        memset((void *)str, 0, sizeof(str));
        sprintf(str, "adc%d", pin);
        p = strstr(buf, str) + strlen(str) + 1;
        sscanf(p, "%d", &ret);
    }
    else
    {
        fprintf(stderr, "%s ERROR: invalid pin, pin=%d\n", __FUNCTION__, pin);
        exit(-1);
    }      
    return ret;

}

void analogWrite(int pin, int value)
{
    char path[128];
    char buf[128];
    char cmd[128];
    int ret = -1;
    int fd = -1;
    int max_level = 0;
    int map_level = 0;
        
    if ( (pin >= 0 && pin <= MAX_PWM_NUM) && 
        (value >= 0 && value <= MAX_PWM_LEVEL) )
    {
        memset((void *)path, 0, sizeof(path));
        sprintf(path, "%s%d/%s", PWM_IF_PREFIX, pin, PWM_IF_MAX);
        fd = open(path, O_RDONLY);
        if ( fd < 0 )
        {
            fprintf(stderr, "open %s failed\n", path);
            exit(-1);
        }
        
        ret = read(fd, buf, sizeof(buf));
        
        if ( ret <= 0 )
        {
            fprintf(stderr, "read %s failed\n", path);
            close(fd);
            exit(-1);
        }
        
        max_level = atoi(buf);
        map_level = (max_level * value)/MAX_PWM_LEVEL;
        memset((void *)cmd, 0, sizeof(cmd));
        sprintf(cmd, "echo %d > %s%d/%s", 
            map_level, PWM_IF_PREFIX, pin, PWM_IF);
        system(cmd);
    }
    else
    {
        fprintf(stderr, "%s ERROR: invalid pin, pin=%d\n", __FUNCTION__, pin);
        exit(-1);
    }      
}


extern void setup(void);
extern void loop(void);

int argc;
char **argv;

static void core_init(void)
{
}

int main(int _argc, char **_argv)
{
    argc = _argc;
    argv = _argv;
    
    core_init();
    
    setup();
    while(1)
    {
        loop(); 
    }
    return 0;
}

