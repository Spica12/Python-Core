"""
У компанії є кілька відділів. Список працівників для кожного відділу має такий 
вигляд:

['Robert Stivenson,28', 'Alex Denver,30']

Це список рядків із прізвищем та віком співробітника, розділеними комами.

Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про 
кожного співробітника починалася з нового рядка.

Функція запису в файл write_employees_to_file(employee_list, path), де:
- path – шлях до файлу.
- employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
  [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

Вимоги:
- запишіть вміст employee_list у файл, використовуючи режим "w".
- ми поки що не використовуємо менеджер контексту with
- кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:

  Robert Stivenson,28
  Alex Denver,30
  Drake Mikelsson,19

--------------------------------------------
def write_employees_to_file(employee_list, path):
0
"""
def write_employees_to_file(employee_list, path):
    print(path)

    try:
        file = open(path, 'w') # , encoding='utf-8')
        print('File opened')

        try:
            print('Good, we can write to file')
            
            for element in employee_list:
                for under_element in element:
                    print(f'- Add to file emloyee: {under_element}')
                    file.write(f'{under_element}\n')              
          
        except OSError:
            print('Error. Cann\'t read the file')
        finally:
            print('Writing have finished')
            file.close()

    except:
        print('Error. Cann\'t open file.')



employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = 'Modul_6_Work with files/Autocheck_Modul_6/6_exe_2.txt'
    
write_employees_to_file(employee_list, path)
