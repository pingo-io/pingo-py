import pyupm_i2clcd as lcd

lcd_display = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcd_display.setColor(0, 0, 255)
lcd_display.setCursor(0,0)
lcd_display.write('Hello World!')
