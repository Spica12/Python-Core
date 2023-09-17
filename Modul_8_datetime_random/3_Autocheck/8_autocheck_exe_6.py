"""
Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме 
середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. 
Параметр number_list — список чисел

Увага
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:

виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
-------------------------------------------------------------------------
from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    getcontext().prec = signs_count

    average_sum = Decimal(0)
    for el in number_list:
        average_sum += Decimal(el)

    len_numbers = Decimal(len(number_list))
    
    average = average_sum / len_numbers
    print(average_sum, len_numbers, average)

    return average

print(decimal_average([3, 5, 77, 23, 0.57], 6) == Decimal(21.714))
print(decimal_average([31, 55, 177, 2300, 1.57], 9) == Decimal(512.91400))
