import time
import board
import adafruit_ds3231

i2c = board.I2C()  
rtc = adafruit_ds3231.DS3231(i2c)
t = rtc.datetime
print(t)