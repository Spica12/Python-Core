from datetime import datetime


"""
Розробіть функцію get_days_from_today(date), яка повертатиме кількість 
днів від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

Підказки:

Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.
---------------------------------------------------------------------
from datetime import datetime


def get_days_from_today(date):
"""


def get_days_from_today(date):

    date = date.split('-')
    some_date = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])).date()

    current_date = datetime.today().date()
    print(current_date)
    
    delta = current_date - some_date

    return delta.days


some_date = '2020-10-09'

print(get_days_from_today(some_date))
print(get_days_from_today('2021-10-09'))