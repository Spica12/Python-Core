"""
У модулі 5 ми написали функцію sanitize_phone_number для нормалізації 
рядка з телефонним номером. Нагадаємо, що при отриманні рядків

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",

Ми отримували наступний вивід:

380501233234
0503451234
0508889900
380501112222
380501112211

Уявіть, що в іншому місці програми у нас виникла вимога зробити висновок у форматі

+380501233234
+380503451234
+380508889900
+380501112222
+380501112211

І тут ідеально підійде створення декоратора для функції sanitize_phone_number. 
Декоратор повинен додавати для коротких номерів префікс +38, а для повного 
міжнародного номера (з 12 символом) - тільки знак +. Реалізуйте декоратор 
format_phone_number для функції sanitize_phone_number з необхідним функціоналом.
-------------------------------------------------------------------------------
def format_phone_number(func):


@format_phone_number
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
"""


def format_phone_number(func):
    
    def inner(phone):
            
            phone = func(phone)
            
            if len(phone) == 10:
                new_phone = '+38' + phone
            elif len(phone) == 12:
                new_phone = '+' + phone


            return new_phone
    
    return inner
        

        
            
        
            
        
    


@format_phone_number
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


numbers = {
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
}

for phone in numbers:
    print(sanitize_phone_number(phone))