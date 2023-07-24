# Створити порожній кортеж
my_tuple = tuple()
another_tuple = ()

# Створити непустий кортеж
not_empty = (1, 2, 3)
other_tuple = 4, 5

# Створити кортеж з одним елементом
single_tuple = (7,)

# Доступ до елемента кортежу
not_empty = (1, 2, 3)

print(not_empty[0]) # 1
print(not_empty[1]) # 2
print(not_empty[2]) # 3

# Кортежі зручні у множинному привласненні
x, y = 1, 2 
x, y = y, x