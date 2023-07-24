# Другий етап. Необхідно написати функцію is_valid_password, яка 
# перевірятиме отриманий параметр — пароль на надійність.

# Критерії надійного пароля:

# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.

# Функція is_valid_password повинна повернути True, якщо 
# переданий параметр пароль відповідає вимогам на надійність. 
# Інакше повернути False.
# ----------------------------------------------
# def is_valid_password(password):
# ----------------------------------------------
from exe_10 import get_random_password


def is_valid_password(password):

    is_len = False
    has_upper = False
    has_lower = False
    has_digital = False

    if len(password) == 8:
        is_len = True

    for char in password:
        
        if ord(char) >= 65 and ord(char) <= 90:
            has_upper = True
        elif ord(char) >= 97 and ord(char) <= 122:
            has_lower = True
        elif ord(char) >= 48 and ord(char) <= 57:
            has_digital = True
    
    # print('is_len: ', is_len)
    # print('has_upper: ', has_upper)
    # print('has_lower: ', has_lower)
    # print('has_digital: ', has_digital)
    
    return is_len and has_upper and has_lower and has_digital
            

if __name__ == '__main__':
    
    new_password = get_random_password()
    print(new_password, is_valid_password(new_password))

    password_1 = 'ghjkSFGk'
    print(password_1, is_valid_password(password_1))

    password_1 = 'ghjk8FGk'
    print(password_1, is_valid_password(password_1))


