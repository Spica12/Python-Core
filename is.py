value_one = 5 
value_two = 5

# ----------------------    is    ----------------------

# Відображаються ідентичності і рівності змінних
print('Are values equal? - ', value_one == value_two)
print('Are values identical? - ', value_one is value_two)

# Перевірка місця збереження у пам'яті
print('Path of value in memory', id(value_one))
print('Path of value in memory', id(value_two))