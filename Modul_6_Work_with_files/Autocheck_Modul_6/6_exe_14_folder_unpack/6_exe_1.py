"""
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
"""
# def total_salary(path):

def total_salary(path):
    total_salary = 0.0

    try:
        file = open(path, 'r', encoding='utf-8')

        try:
            line = file.readline()

            while line != '':
                line = line.rstrip()
                print(f'{line!r}')

                worker = list(line.split(','))
                total_salary += float(worker[1])
                line = file.readline()

        except OSError:
            print('File {path} cann\'t read')
        finally:
            file.close()

    except OSError:
        print('File {path} cann\'t open')    

    return total_salary


my_path = 'D:/GoIT/Python Core/Modul_6_Work with files/Autocheck_Modul_6/6_exe_1.txt'

print(total_salary(my_path))