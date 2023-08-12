"""
Ваша компанія проводить маркетингові кампанії за допомогою 
SMS-розсилок. Автоматичний збір телефонних номерів із бази даних 
формує певний перелік. Але клієнти залишають свої номери у 
довільному вигляді:

"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",

Сервіс розсилок чудово розуміє і може відправити SMS клієнту, 
тільки якщо телефонний номер містить правильні цифри. Необхідно 
реалізувати функцію sanitize_phone_number, яка прийматиме рядок 
з телефонним номером та буде нормалізувати його, тобто. буде 
прибирати символи (, -, ), + та пробіли.

Результат:
380501233234
0503451234
0508889900
380501112222
380501112211
------------------------------------------------
def sanitize_phone_number(phone):
"""

def sanitize_phone_number(phone: str) -> str:

    phone = phone.strip()\
            .replace(' ', '')\
            .replace('(', '')\
            .replace(')', '')\
            .replace('-', '')\
            .replace('+', '')

    return phone


phone_number = "    +38(050)123-32-34"
print(f'{phone_number!r:}\t -> {sanitize_phone_number(phone_number)!r}')

phone_number = "     0503451234"
print(f'{phone_number!r:}\t -> {sanitize_phone_number(phone_number)!r}')

phone_number = "(050)8889900"
print(f'{phone_number!r:}\t -> {sanitize_phone_number(phone_number)!r}')

phone_number = "38050-111-22-22"
print(f'{phone_number!r:}\t -> {sanitize_phone_number(phone_number)!r}')

phone_number = "38050 111 22 11   "
print(f'{phone_number!r:}\t -> {sanitize_phone_number(phone_number)!r}')
