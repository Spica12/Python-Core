hello_str = 'Hello'

hello_str.upper()
print(hello_str.upper()) # HELLO
print(hello_str) # Hello

hello_str.lower()
print(hello_str.lower()) # hello
print(hello_str) # hello

print(hello_str.startswith('Hel')) # True
print(hello_str.startswith('hel')) # False

print(hello_str.endswith('lo')) # True
print(hello_str.endswith('LO')) # False

#  -------------------------------------------
# Робота з елементами
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

my_list = ['a', 'b', 'c']
for i in my_list:
    print(i)
# a
# b
# c

# Робота з індексами

my_list = ['a', 'b', 'c']
for i in range(len(my_list)):
    print(my_list[i])
# a
# b
# c

# Робота і з елементами і з індексами
my_list = ['a', 'b', 'c']
for i, element in enumerate(my_list):
    print(i, element)
# 0 a
# 1 b
# 2 c

my_list = ['a', 'b', 'c']
for i in reversed(my_list):
    print(i)
# c
# b
# a

my_list = ['e', 'c', 'b', 'a']
for i in sorted(my_list):
    print(i)
# a
# b
# c
# e