# KK 2nd Boolean Notes

import time
import datetime as date

over = False
print(over)
# ^ waste of space and time

name = "0"
print(name.isdigit()) # True
value = "LaRose"
print(value.isupper()) # False

current_time = time.time()
readable_time = time.ctime(current_time)
print(f"Current time in seconds since January 1, 1970 (epoch time): {current_time}")
print(f"Current time: {readable_time}")

now = date.datetime.now()
hour = now.strftime("%H")
# month number = %m
# month = %b or %B
# day = %d
# year = %Y: full year %y: 2 digit year
# hour = %H
# minutes = %M
# seconds = %S

print(f"Current time according to datetime: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is a STRING: {isinstance(hour, str)}")
print(f"My hour variable is an INTEGER: {isinstance(hour, int)}")
print(f"My hour variable is a FLOAT: {isinstance(hour, float)}")


