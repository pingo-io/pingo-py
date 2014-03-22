#ifndef _ARDUINO_A10_H_
#define _ARDUINO_A10_H_

#undef MAX_GPIO_NUM
#define MAX_GPIO_NUM 19

#undef MAX_GPIO_MODE_NUM
#define MAX_GPIO_MODE_NUM 8

#undef MAX_PWM_NUM
#define MAX_PWM_NUM 5

#undef MAX_ADC_NUM
#define MAX_ADC_NUM 5

/*
* all digital I/O can be read/write via sysfs interface
*/
#define GPIO_MODE_DIR "/sys/devices/virtual/misc/gpio/mode/"
#define GPIO_PIN_DIR "/sys/devices/virtual/misc/gpio/pin/"
#define GPIO_IF_PREFIX "gpio"

/*
* read adc value from /proc/adc, the format is:
adc0:63
adc1:63
*/
#define ADC_IF "/proc/adc"

#define PWM_IF_PREFIX "/sys/class/leds/pwm"
#define PWM_IF_MAX "max_brightness"
#define PWM_IF "brightness"

#endif
