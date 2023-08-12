my_string = 'Hello my little friends!'

print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('Hel'))
print(my_string.startswith('hel'))
print(my_string.endswith('s!'))
print(my_string.endswith('S!'))

print(my_string.capitalize()) # Перша буква велика
print(my_string.title()) # Кожна перша буква з великої

print(my_string.count('e'))


my_list = [1]
print(type(my_list), id(my_list), my_list, sep='\t')

my_list.append(2)
print(type(my_list), id(my_list), my_list, sep='\t')

my_list = (1, )
print(type(my_list), id(my_list), my_list, sep='\t')

my_list = (1, 2)
print(type(my_list), id(my_list), my_list, sep='\t')