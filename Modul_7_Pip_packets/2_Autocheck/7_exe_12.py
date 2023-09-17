from pathlib import Path, PurePath


"""
Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), 
яка додає додаткову інформацію в файл на шляху path з параметра additional_info, 
і після цього повертає рядок з позиції start_pos довжиною count_chars.

Вимоги:

функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
записувати в кінець файлу рядок additional_info
після запису функція має відкрити той самий файл для читання
прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.

-------------------------------------------------------------------------
def file_operations(path, additional_info, start_pos, count_chars):
"""

def file_operations(path, additional_info, start_pos, count_chars):
    find_info = ''

    with open(path, 'a') as file:
        file.write(additional_info)

    with open(path, 'r') as file:
        file.seek(start_pos)
        find_info = file.read(count_chars)
    
    return find_info


my_path = PurePath('7_exe_12.txt')
additional_info = 'some info'

print(file_operations(my_path, additional_info, 3, 3))