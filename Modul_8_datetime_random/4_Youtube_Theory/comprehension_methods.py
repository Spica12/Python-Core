
print('------------------------------------------------ .comprehensions()')

my_list = list()
for i in range(10):
    my_list.append(i)

print(my_list)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_second_list = [i for i in range(10)]
print(my_second_list)       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('------------------------------------------------ .comprehensions()')

my_list = list()
for i in range(10):
    my_list.append(i * 10)

print(my_list)              # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

my_second_list = [i*10 for i in range(10)]
print(my_second_list)       # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print('------------------------------------------------ .comprehensions()')

my_list = list()
for i in range(10):
    if i % 2:
        my_list.append(i * 10)

print(my_list)              # [10, 30, 50, 70, 90]

my_second_list = [i*10 for i in range(10) if i%2]
print(my_second_list)       # [10, 30, 50, 70, 90]

print('------------------------------------------------ .comprehensions()')

my_second_list = [i*10 if i%2 else 123 for i in range(10)]
print(my_second_list)       # [123, 10, 123, 30, 123, 50, 123, 70, 123, 90]

print('------------------------------------------------ .comprehensions()')

my_dict = {i: el for i, el in enumerate(['a', 'b', 'c'])}
print(my_dict)              # {0: 'a', 1: 'b', 2: 'c'}

print('------------------------------------------------ .comprehensions()')
my_set= {i for i in enumerate(['a', 'b', 'c'])}
print(my_set)               # {(0, 'a'), (1, 'b'), (2, 'c')}