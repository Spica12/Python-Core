from datetime import datetime, timedelta

print('------------------------------------ datetime.now()')
current_dt = datetime.now() 
print(f'{current_dt = }')   # datetime.datetime(2023, 9, 2, 20, 27, 27, 568749)
print(current_dt)           # 2023-09-02 20:29:01.719532

print('------------------------------------ .year')
current_year = current_dt.year
print(current_year)         # 2023

print('------------------------------------ .month')
current_month = current_dt.month
print(current_month)        # 9

print('------------------------------------ .day')
current_day = current_dt.day
print(current_day)          # 2

print('------------------------------------ .hour')
current_hour = current_dt.hour
print(current_hour)         # 20

print('------------------------------------ .minute')
current_minute = current_dt.minute
print(current_minute)       # 37

print('------------------------------------ .second')
current_second = current_dt.second
print(current_second)       # 12

print('------------------------------------ .microsecond')
current_microsecond = current_dt.microsecond
print(current_microsecond)  # 304499

print('------------------------------------ .date()')
# Повертає дату
current_date = current_dt.date()
print(current_date)         # 2023-09-02

print('------------------------------------ .time()')
# Повертає дату
current_time = current_dt.time()
print(current_time)         # 20:40:26.760023

print('------------------------------------  datetime(year, month, hour, minute, second, microsecond)')
custom_dt = datetime(year=1970, month=1, day=1, hour=0, minute=1)
print(custom_dt)            # 1970-01-01 00:01:00 

print('------------------------------------ .weekday()')
# Визначити день тижня
# Monday    - 0
# Tuesday   - 1
# Wednesday - 2
# Thursday  - 3
# Friday    - 4
# Saturday  - 5
# Sunday    - 6
custom_weekday = custom_dt.weekday()
print(custom_weekday)       # 3

print('------------------------------------------------ .timedelta()')
delta = timedelta(weeks=1)
custom_dt_delta_weeks = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_weeks}')        
# 1970-01-01 00:01:00 --> 7 days, 0:00:00 --> 1970-01-08 00:01:00

delta = timedelta(days=1)
custom_dt_delta_days = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_days}')        
# 1970-01-01 00:01:00 --> 1 day, 0:00:00 --> 1970-01-02 00:01:00

delta = timedelta(hours=1)
custom_dt_delta_hours = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_hours}')        
# 1970-01-01 00:01:00 --> 1:00:00 --> 1970-01-01 01:01:00

delta = timedelta(minutes=1)
custom_dt_delta_minutes = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_minutes}')        
# 1970-01-01 00:01:00 --> 0:01:00 --> 1970-01-01 00:02:00

delta = timedelta(seconds=1)
custom_dt_delta_seconds = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_seconds}')        
# 1970-01-01 00:01:00 --> 0:00:01 --> 1970-01-01 00:01:01

delta = timedelta(microseconds=1)
custom_dt_delta_microseconds = custom_dt + delta
print(f'{custom_dt} --> {delta} --> {custom_dt_delta_hours}')        
# 1970-01-01 00:01:00 --> 0:00:00.000001 --> 1970-01-01 01:01:00

print('------------------------------------------------ .strftime()')
# %a    Abbreviated weekday name                                Sun, Mon, ...
# %A    Full weekday name                                       Sunday, Monday, ...
# %w    Weekday as a decimal number                             0, 1, ..., 6
# %d    Day of the month as a zero-padded decimal               01, 02, ..., 31
# %-d   Day of the month as a decimal number                    1, 2, ..., 31
# %b    Abbreviated month name                                  Jan, Feb, ... Dec
# %B    Full month name                                         January, February, ...
# %m    Month as a zero-padded decimal number                   01, 02, ..., 12
# %-m   Month as a decimal number                               1, 2, ..., 12
# %y    Year without century as a zero-padded decimal number    00, 01, ... 99
# %-y   Year without century as a decimal number                0, 1, ..., 23
# %Y    Year with century as a decimal number                   2013, 2019 etc.
# %H    Hour (24-hour clock) as a zero-padded decimal number    00, 01, ..., 23
# %-H   Hour (24-hour clock) as a decimal number                0, 1, ..., 23
# %I    Hour (12-hour clock) as a zero-padded decimal number    01, 02, ..., 12
# %-I   Hour (12-hour clock) as a decimal number                1, 2, ..., 12
# %p    Locale's AM or PM                                       AM, PM
# %M    Minute as a zero-padded decimal number                  00, 01, ..., 59
# %-M   Minute as a decimal number                              0, 1, ..., 59
# %S    Second as a zero-padded decimal number                  00, 01, ..., 59
# %-S   Second as a decimal number                              0, 1, ..., 59
# %f    Microsecond as a zero-padded decimal number             000000 - 999999
# %z    UTC offset in the form + HHMM or -HHMM
# %Z    Time zone name
# %j    Day of the year as a zero-padded decimal number         001, 002, ..., 366
# %-j   Day of the year as a decimal number                     1, 2, ..., 365

# %U    Week number of the year (Sunday as the first day of
#       the week). All days in a new year preceding the first
#       Sunday are considered to be in week 0.                  00, 01, ..., 53

# %W    Week number of the year (Monday as the first day of
#       the week). All days in a new year preceding the first
#       Monday are considered to be in week 0.                  00, 01, ..., 53 
# %c    Locale's appropriate date and time representation       Mon Sep 30 07:06:05 2013
# %x    Locale's appropriate date representation                09/30/13
# %X    Locale's appropriate time representation                07:06:05
# %%    A Literal '%' character                                 %                               

now = datetime.now()
print(now)
#2023-09-02 21:56:10.769716
print(now.strftime('%a'))                     # Sat
print(now.strftime('%a %d.%m.%Y %H:%M'))      # Sat 02.09.2023 22:33  

print('------------------------------------------------ .strptime()')
custom_dt_strptime = datetime.strptime('Sat 02.09.2023 22:33', '%a %d.%m.%Y %H:%M')
print(custom_dt_strptime)                     # 2023-09-02 22:33:00

print('------------------------------------------------ .timestamp()')
custom_timestamp = custom_dt_strptime.timestamp()
print(custom_timestamp)                       # 1693683180.0

print('------------------------------------------------ .fromtimestamp()')
custom_fromtimestamp = datetime.fromtimestamp(1693683180.0)
print(custom_fromtimestamp)                   # 2023-09-02 22:33:00
