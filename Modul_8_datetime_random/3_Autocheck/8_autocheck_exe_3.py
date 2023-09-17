"""
Напишіть функцію get_str_date(date), яка перетворюватиме дату з 
бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді 
наступного рядка 
'Thursday 27 May 2021' - день тижня, число, місяць та рік. 

Перетворене значення функція повертає під час виклику.
-------------------------------------------------------------
from datetime import datetime


def get_str_date(date):
"""

from datetime import datetime


def get_str_date(date):
    print(date)
    new_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    print(new_date)
    new_format = datetime.strftime(new_date, '%A %d %B %Y')
    print(new_format)
    
    return new_format


print(get_str_date('2021-05-27 17:08:34.149Z'))