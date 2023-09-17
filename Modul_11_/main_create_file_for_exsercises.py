from pathlib import Path
import os

# Tasks:
# | | Add func check dir, if not - create dir
# | | Create own packet with pip


MODUL = 11

TYPE_FILE = '.py'

TYPES = {
    1: 'theory',
    2: 'practice',
    3: 'you_theory',
    4: 'you_practice',
    5: 'you_add',
    6: 'autocheck'
}
for key, type in TYPES.items():
    print(f'{key} - {type}')

while True:
    try:
        user_input = int(input('Choose type of file: '))
        break
    except TypeError:
        print('Wrong number. Try again')


# Отриммуємо шлях до папки де треба зробити шаблон
my_path = os.path.abspath(__file__ + '\..')
my_path = Path(my_path)
print(my_path)


for number, file in enumerate(my_path.iterdir()):
    pass

next_number_file = number + 1

while True:
    try:
        user_input_explanation = input('Enter the short explanation of file: ').split()
        user_input_explanation = '_'.join(user_input_explanation)
        break
    except TypeError:
        print('Something wrong. Try again')

file_name = '_'.join((str(MODUL), 
                      TYPES[user_input], 
                      str(next_number_file), 
                      user_input_explanation))

path_of_new_file = os.path.abspath(f'{my_path}\{file_name}{TYPE_FILE}')
print(file_name)

with open(path_of_new_file, 'w') as file:
    print(f'File: {file_name} created. Path: {path_of_new_file}')