from datetime import datetime, timedelta


day_2021 = datetime(year=2021, month=4, day=7, hour=12)
print(day_2021)

day_2022 = datetime(year=2022, month=7, day=2, hour=16)
print(day_2022)

ts = day_2021.timestamp()
print(ts)

print(day_2022.timestamp() - day_2021.timestamp())