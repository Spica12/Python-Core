# Списки (list)
# Впорядкований змінюваний конетйнер
my_list = list()

empty_list = []

not_empty = [1, 2, 'user']

# Доступ до елементу
# Індекс починається з нуля
some_iterable = ['a', 'b', 'c']

first_letter = some_iterable[0] # 'a'
second_letter = some_iterable[1] # 'b'
third_letter = some_iterable[2] # 'c'

# Доступ до елементу через індексування з кінця
first_letter = some_iterable[-3] # 'a'
second_letter = some_iterable[-2] # 'b'
third_letter = some_iterable[-1] # 'c'

# Можливість змінювати елементи списку
some_iterable = ['a', 'b', 'c']

some_iterable[1] = 'Z'
print(some_iterable[1]) # 'Z'

# Зрізи (Slice)
some_string = 'This is awesome string'
first_five = some_string[0:5]
print(first_five) # 'This '

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:9:2] # З 1(інд 0) по 10(інд 9), крок 2
even_numbers = numbers[1:9:2] # З 2(інд 1) по 10(інд 9), крок 2
three_numbers = numbers[2:9:3] # З 3(інд 2) по 10(інд 9), крок 3
print(odd_numbers) # [1, 3, 5, 7, 9]
print(even_numbers) # [2, 4, 6, 8]
print(three_numbers) # [3, 6, 9]

# Можна не вказувати перший або останній індекс
# Буде взято перший або останній індекс
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

# Зріз який бере всі елементи з кроком 1 (копіює список)
numbers_copy = numbers[:]

# В ЗРІЗ НЕ ВХОХИТЬ ЕЛЕМЕНТ ДО ЯКОГО БРАТИ ЕЛЕМЕНТИ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_three = numbers[0:3] # [0, 1, 2]
