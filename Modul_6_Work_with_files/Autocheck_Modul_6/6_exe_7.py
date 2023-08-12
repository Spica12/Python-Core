"""
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:
- прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
- запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
- запис нового вмісту файлу output має бути одноразовий і використовувати метод write
-------------------------------------
def sanitize_file(source, output):
"""
def sanitize_file(source, output):
    data = ''
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    with open(source, 'r') as file:
        while True:
            symbol = file.read(1)
            if len(symbol) == 0:
                break
            elif symbol not in numbers:
                data += symbol
    
    print(data)

    with open(output, 'w') as file:
        file.write(data)


path_source = 'D:/GoIT/Python Core\Modul_6_Work with files/Autocheck_Modul_6/6_exe_7_source.txt'
path_output = 'D:/GoIT/Python Core\Modul_6_Work with files/Autocheck_Modul_6/6_exe_7_output.txt'

sanitize_file(path_source, path_output)