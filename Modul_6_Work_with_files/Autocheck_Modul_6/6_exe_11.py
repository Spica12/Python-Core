"""
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

- path – шлях до файлу.

Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e

Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']

Вимоги:
- Використовуйте менеджер контексту для читання з файлу
----------------------------------------------------------
def get_credentials_users(path):
"""

def get_credentials_users(path):
    users_password = list()

    with open(path, 'rb') as file:

        for line in file.readlines():
            line = line.decode().rstrip()
            users_password.append(line)

    return users_password


path = 'Modul_6_Work_with_files/Autocheck_Modul_6/6_exe_10.bin'

users_password = get_credentials_users(path)
print(users_password)