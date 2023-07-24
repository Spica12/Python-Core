# І, нарешті, третій, останній етап. Використовуючи рішення із 
# попередніх двох завдань, напишіть функцію get_password, яка 
# згенерує нам випадковий надійний пароль та поверне його. 
# Алгоритм простий — ми генеруємо пароль за допомогою функції 
# get_random_password і, якщо він проходить перевірку на 
# надійність функцією is_valid_password, повертаємо його, 
# якщо ні — повторюємо ітерацію знову.

# Примітка: Хорошою практикою буде обмежити кількість спроб 
# (наприклад, до 100), щоб не отримати нескінченний цикл.

#  ------------------------------------------------
# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result


# def is_valid_password(password):
#     if len(password) != 8:
#         return False

#     has_upper = False
#     has_lower = False
#     has_num = False

#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True

#     return has_upper and has_lower and has_num


# def get_password():
#  ------------------------------------------------
from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

# 1. Згенерувати пароль
# 2. Перевірити на валідність
# 3. Занести все в цикл
# 4. Обмежити кількість спроб до 100

def get_password():

    count = 0

    while True:

        if count >= 100:
            new_password = None
            break

        new_password = get_random_password()
        is_valid = is_valid_password(new_password)

        if is_valid:
            break
        else:
            count += 1

    return new_password


print(get_password())