from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)                 # 2023-08-29 20:02:21.085524

interval = timedelta(days=45)
print(current_date + interval)      # 2023-10-13 20:02:21.085524


day_off = current_date - interval
day_on = current_date + interval
print(day_on - day_off)             # 90 days, 0:00:00



