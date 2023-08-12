"""
Повернемося до нашого завдання із телефонними номерами. 
Компанія розширюється та вийшла на ринок Азії. Тепер у списку 
можуть знаходитись телефони різних країн. Кожна країна має свій 
телефонний код .

Компанія працює з наступними країнами

---------------------------------
|   Країна  | Код ISO | Префікс |
---------------------------------
| Japan     |    JP   |   +81   |
| Singapore |    SG   |   +65   |
| Taiwan    |    TW   |   +886  |
| Ukraine   |    UA   |   +380  |
---------------------------------

Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно 
створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

1 - Приймати список телефонних номерів.
2 - Санітизувати (нормалізувати) отриманий список телефонів 
    клієнтів за допомогою нашої функції sanitize_phone_number.
3 - Сортувати телефонні номери за вказаними у таблиці країнами.
4 - Повертати словник зі списками телефонних номерів для кожної 
    країни у такому вигляді:

{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}

5 - Якщо не вдалося порівняти код телефону з відомими, цей 
    телефон повинен бути доданий до списку словника з ключем 'UA'.
-------------------------------------------------------------
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
"""
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):

    normal_phones = {'UA': [],
                    'JP': [],
                    'TW': [],
                    'SG': []
                    }               

    for phone in list_phones:

        phone = sanitize_phone_number(phone)
        
        if phone.find('81', 0, 3) == 0:
            normal_phones['JP'].append(phone)

        elif phone.find('886', 0, 3) == 0:
            normal_phones['TW'].append(phone)

        elif phone.find('65', 0, 3) == 0:
            normal_phones['SG'].append(phone)

        else:
            normal_phones['UA'].append(phone)

    return normal_phones


# list_phones = (
#     '     +81 641 365 56 36',
#     '  65 965 234 63 74',
#     '+886 641 365 56 36',
#     '     +380 147 425 74 63',
#     '+380 (063) 760 96 40',
#     '+81 674 853 31 74',
#     '+886 102-732-00-00',
# )

list_phones = ['0658759411',
               '818765347',
               '818765344',
               '8867658976',
               '657658976'
               ]


print(get_phone_numbers_for_countries(list_phones))
