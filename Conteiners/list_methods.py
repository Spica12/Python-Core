# Додавання нового елементу в кінець списку -            append
numbers = ['a', 'b']

numbers.append('c')
print(numbers) # ['a', 'b', 'c']

# Очистити список -                                       clear
num = [1, 2, 3]

num.clear()
print(num) # []

# Видалення елементу зі списку. Помилка, якщо немає -     remove
chars = ['a', 'b']

chars.remove('b')
print(chars) # ['a']

# Повернути елемент та видалити його зы списку -          pop
chars = ['a', 'b', 'c']

last = chars.pop(1)
print(chars) # ['a', 'c']
print(last) # 'b'

# Розширити список іншими елементами -                    extend
chars = ['a', 'b']
numbers = [1, 2]

chars.extend(numbers)
print(chars) # ['a', 'b', 1, 2]

# Вставити елемент на позицію з індексом -                insert
chars = ['a', 'b']

chars.insert(1, 'c')
print(chars) # ['a', 'c', 'b']

# Знайти індекс першого елемента у списку -               index
chars = ['a', 'b', 'c', 'a']

a_index = chars.index('a')
print(a_index) # 0

# Повернути кількість елементів у списку -                count
chars = ['a', 'b', 'c', 'a']

a_count = chars.count('a')
print(a_count) # 2

# Відсортувати список за зростанням -                     sort
# list.sort(key=None, reverse=False)
chars = ['z', 'a', 'b']

chars.sort()
print(chars) # ['a', 'b', 'z']

# Змінити порядок елементів у списку на зворотній -       reverse
chars = ['a', 'b', 'c']

chars.reverse()
print(chars) # ['c', 'b', 'a']

# Повернути копію списку -                                copy
chars = ['a', 'b', 'c']
chars_copy = chars.copy()

print(chars == chars_copy) # True


