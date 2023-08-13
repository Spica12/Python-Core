"""
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19

Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']

Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. 
Його необхідно прибирати при додаванні прочитаного рядка до списку.

Вимоги:

- прочитайте вміст файлу за допомогою режиму "r".
- ми поки що не використовуємо менеджер контексту with
- поверніть із функції список співробітників із файлу
-------------------------------------------------------
def read_employees_from_file(path):

"""


def read_employees_from_file(path):
    employees = list()
    print(path)
    
    try:
        file = open(path, 'r')
        print('File opened')

        try:
            for line in file.readlines():
                employees.append(line.rstrip())

        except OSError:
            print('Error. Cann\'t read from file')

        finally:
            file.close()

        return employees
    
    except OSError:
        print('Error. Cann\'t open file!')

    



path = 'D:/GoIT/Python Core/Modul_6_Work with files/Autocheck_Modul_6/6_exe_2.txt'

employees_list = read_employees_from_file(path)
print(employees_list)