'''
# Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.

# --------------------------------------------
# def is_equal_string(utf8_string, utf16_string):
# '''

def is_equal_string(utf8_string, utf16_string):

    print(f'{utf8_string = }')
    print(f'{utf16_string = }')

    utf8_string = utf8_string.decode().casefold()
    utf16_string = utf16_string.decode('utf-16').casefold()

    if utf8_string == utf16_string:
        return True
    else:
        return False

first_string = 'Hello'.encode()
second_string = 'Hell0'.encode('utf-16')

print(is_equal_string(first_string, second_string))