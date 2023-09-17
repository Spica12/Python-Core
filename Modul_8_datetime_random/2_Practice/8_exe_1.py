from datetime import datetime, date

"""
Напишіть функцію, що приймає на вхід три цілих числа: день, місяць і рік. 
Функція повинна повертати порядковий номер заданого дня в зазначеному 
році і також день тижня.

Порядкова дата містить номер року і порядковий номер дня в цьому році - 
обидва в цілочисельному форматі. При цьому рік може бути будь-яким згідно 
з григоріанським календарем, а номер дня - числом в інтервалі від 1 до 366
"""

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def day_of_year(full_date):
    year, month, day = [int(i) for i in full_date.split('-')]
    day_of_week = datetime(day=day, month=month, year=year).weekday()

    day_zero = date(year, 1, 1).toordinal() - 1
    current_day = date(year, month, day).toordinal()
    day_from_year_start = current_day - day_zero

    return days_name.get(day_of_week), year , day_from_year_start

print(day_of_year('2021-02-21'))