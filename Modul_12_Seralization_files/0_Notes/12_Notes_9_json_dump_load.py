"""
Упакування у відкритий файл та розпакування з файлу.

dump, load упаковує у відкритий для byte-запису файл та 
розпаковує із відкритого для byte-читання файлу.
"""


import json

some_data = {'key': 'value', 
             2: [1, 2, 3], 
             'tuple': (5, 6), 
             'a': {'key': 'value'}
}

file_name = '12_Notes_9_json_dump_load'
extension = '.json'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"
file_full_name = path + file_name + extension

with open (file_full_name, 'w') as fh:
    json.dump(some_data, fh)

with open(file_full_name, 'r') as fh:
    unpacked = json.load(fh)

