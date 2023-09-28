"""
dump, load упаковує у відкритий для byte-запису файл та розпаковує із відкритого для byte-читання файлу.
"""
import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}


file_name = '12_Notes_5_pickle_dump_load'
extension = '.txt'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"

file_full_name = path + file_name + extension

# pickle серелізація - dump
with open(file_full_name, 'wb') as fh:
    pickle.dump(some_data, fh)

# pickle десерелізація - load
with open(file_full_name, 'rb') as fh:
    unpacked = pickle.load(fh)

# Перевірка
print(unpacked)                 # {(1, 3.5): 'tuple', 2: [1, 2, 3], 'a': {'key': 'value'}}
print(some_data == unpacked)    # True
print(some_data is unpacked)    # False


print('----------------- Перевірка читання з минулого файлу-------------------')

file_name = '12_Notes_3_pickle_dumps_loads'
extension = '.bin'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"

with open(path + file_name + extension, 'rb') as fh:
    raw_data = fh.read()
    unpacked = pickle.loads(raw_data)

print(unpacked)                 # {(1, 3.5): 'tuple', 2: [1, 2, 3], 'a': {'key': 'value'}}
print(some_data == unpacked)    # True
print(some_data is unpacked)    # False

# Все теж працює=)
