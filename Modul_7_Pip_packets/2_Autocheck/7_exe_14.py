from pathlib import PurePath

"""
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме 
вміст файлу, додаватиме до прочитаних рядків порядковий номер і 
\зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, 
двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
---------------------------------------------
def to_indexed(source_file, output_file):
"""

def to_indexed(source_file, output_file):

    with open(source_file, 'r') as file:
        source_data = file.readlines()

    with open(output_file, 'w') as file:
        for indx, line in enumerate(source_data):
            file.write(f'{indx}: {line}')


    
        


to_indexed('7_exe_14_source.txt', '7_exe_14_output.txt')