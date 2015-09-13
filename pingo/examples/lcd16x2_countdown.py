""" A countdown in a 16x2 LCD.
It is possible to pause or reset the countdown using buttons.
When the countdown ends buzzes continuously.

Requires:
- Adafruit_CharLCD (https://github.com/adafruit/Adafruit_Python_CharLCD)

Hardware:
- 16x2 LCD (8 digital pins)
- Buzzer (1 digital pin)
- 2x buttons (1 digital pin each)

"""


import time
import pingo

import Adafruit_CharLCD.Adafruit_CharLCD as LCD


lcd, buzzer, pause, pause_status, reset, countdown, COUNTDOWN = (None,) * 7


def startup():
    global lcd, buzzer, pause, pause_status, reset, countdown, COUNTDOWN

    # LCD pins
    lcd_rs = 18
    lcd_en = 27
    lcd_d4, lcd_d5, lcd_d6, lcd_d7 = 22, 23, 24, 25

    # LCD config
    lcd_backlight = 4
    lcd_columns = 16
    lcd_rows = 2

    lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns,
              lcd_rows, lcd_backlight)

    board = pingo.detect.get_board()

    # buzzer pin (BOARD)
    buzzer = board.pins[33]
    buzzer.mode = pingo.OUT

    # pause and reset buttons (BOARD)
    pause = board.pins[29]
    pause.mode = pingo.IN
    reset = board.pins[31]
    reset.mode = pingo.IN

    COUNTDOWN = 300
    pause_status = False
    countdown = COUNTDOWN


def beep(interval=0.06, times=4):
    for _ in range(times):
        buzzer.hi()
        time.sleep(interval)
        buzzer.lo()
        time.sleep(interval)


def seconds_to_minutes(seconds):
    minutes = str(countdown / 60).zfill(2)
    seconds = str(countdown % 60).zfill(2)
    return '{} min {} seg'.format(minutes, seconds)


def reset_countdown(delay_seconds=3):
    beep(interval=0.03, times=3)
    for seconds in reversed(range(1, delay_seconds + 1)):
        lcd.clear()
        lcd.message(u'RESETANDO...\n{} sec'.format(seconds))
        time.sleep(1)
    global countdown
    countdown = COUNTDOWN
    lcd.clear()


if __name__ == "__main__":
    startup()
    while True:
        lcd.clear()

        if pause.state == pingo.HIGH:
            pause_status = not pause_status
            lcd.clear()
            beep(interval=0.03, times=2)

        if pause_status:
            lcd.message(u'PAUSADO em\n{}'.format(seconds_to_minutes(countdown)))
            time.sleep(2.5)
            continue

        if reset.state == pingo.HIGH:
            reset_countdown(3)

        if countdown == 0:
            lcd.message(u'Acabou! Acabou!\nO turno acabou!')
            beep()
            time.sleep(0.999)
            continue

        lcd.message(u'Turno acaba em:\n{}'.format(seconds_to_minutes(countdown)))

        time.sleep(0.999)
        countdown -= 1
