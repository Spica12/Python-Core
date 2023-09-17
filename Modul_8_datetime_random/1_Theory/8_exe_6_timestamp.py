from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)                 # 2023-08-29 20:02:21.085524

print(current_date.timestamp())     # 1693328667.238956

day_zero = datetime.fromtimestamp(0)
print(day_zero)                     # 1970-01-01 02:00:00

print(datetime.strptime('1970:01:01 January Jan 03 03 00', '%Y:%m:%d %B %b %H %I %M'))
print(datetime.strptime('28:02:2020', '%d:%m:%Y'))