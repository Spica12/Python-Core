"""
Реалізуйте функцію add_employee_to_file(record, path), яка у файл 
(параметр path - шлях до файлу) буде додавати співробітника 
(параметр record) у вигляді рядка "Drake Mikelsson,19".

Вимоги:

- параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
- кожен запис у файл має починатися з нового рядка.
- необхідно щоб стара інформація у файлі теж зберігалася, тому при 
  роботі з файлом відкрийте файл у режимі 'a', додайте співробітника 
  record у файл і закрийте його
- ми поки що не використовуємо менеджер контексту with
------------------------------------------------------------
def add_employee_to_file(record, path):

"""
def add_employee_to_file(record, path):
    
    try:
        file = open(path, 'a')

        try:
            file.write(f'{record}\n')

        except OSError:
            print('Cann\'t write to the file')
        
        finally:
            file.close()

    except OSError:
        print('Error. Cann\'t open the file')



path = 'D:/GoIT/Python Core/Modul_6_Work with files/Autocheck_Modul_6/6_exe_4.txt'

record = 'Drake Mikelsson,19'

add_employee_to_file(record, path)