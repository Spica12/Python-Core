"""
Напишіть функцію визначення кількості днів у конкретному місяці. 
Ваша функція повинна приймати два параметри: month - номер місяця у 
вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається 
із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
--------------------------------------------------------------
from datetime import date


def get_days_in_month(month, year):
"""

from datetime import date


def get_days_in_month(month, year):

    day = 27

    while True:

        try:
            print(year, month, day)
            some_date = date(year, month, day)
            
           
        except:
            return day-1
        
        day += 1



print(get_days_in_month(month=3, year=2021))


# 2021-03-01
# 2021-03-28
# 2021-03-29
# 2021-03-30
# 2021-03-31