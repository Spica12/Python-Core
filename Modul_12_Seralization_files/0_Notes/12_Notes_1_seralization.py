"""
Серіалізація (у програмуванні) — процес перетворення будь-якої структури даних у 
послідовність байтів. 

Зворотна до операції серіалізації є операція десеріалізації (структуризації) — 
відновлення початкового стану структури даних із бітової послідовності.
"""

expences = {
    'hotel': 10,
    'breakfast': 30,
    'taxi': 15,
    'lunch': 20
}

file_name = '12_Notes_1_seralization.txt'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"


# Користувацька серелізація
with open(path + file_name, 'w') as fh:
    for key, value in expences.items():
        fh.write(f'{key}| {value}\n')


# Користувацька десерелізація
new_expences = dict()

with open(path + file_name, 'r') as fh:
    raw_readlines = fh.readlines()
    for line in raw_readlines:
        key, value = line.split('|')
        new_expences[key] = int(value)

print(new_expences)