"""
dumps запаковує в byte-рядок об'єкт, 
loads розпаковує з byte-рядок в об'єкт. 

Ці методи потрібні, коли ми хочемо контролювати, що робити з byte представленням, 
наприклад, відправити його мережею або прийняти з мережі.
"""

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

# pickle серелізація - dumps
byte_string  = pickle.dumps(some_data)
# pickle десерелізація - loads
unpacked = pickle.loads(byte_string)
# Перевірка
print(unpacked)                 # {(1, 3.5): 'tuple', 2: [1, 2, 3], 'a': {'key': 'value'}}
print(some_data == unpacked)    # True
print(some_data is unpacked)    # False


#  ------------------ My variant this task -------------------

file_name = '12_Notes_3_pickle_dumps_loads'
extension = '.bin'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"

# pickle серелізація - dumps
byte_string  = pickle.dumps(some_data)

with open(path + file_name + extension, 'wb') as fh:
    fh.write(byte_string)

# pickle десерелізація - loads

with open(path + file_name + extension, 'rb') as fh:
    raw_data = fh.read()
    unpacked = pickle.loads(raw_data)

print(unpacked)                 # {(1, 3.5): 'tuple', 2: [1, 2, 3], 'a': {'key': 'value'}}
print(some_data == unpacked)    # True
print(some_data is unpacked)    # False

