my_list = [1, [1, 2],1, 'snake', 'text', 45, 57, 568, True, False]

print(my_list)

my_list = [1, 45, 57, 568, -39, -67, 5, 6, 78]

print(my_list)
print(my_list[2], '', sep='\n')


for elem in my_list:
    if elem <= 20:
        print(elem)

for elem in range(len(my_list)):
    if elem <= 20:
        print(my_list[elem])

print('------------------')
my_list.append(16)
print(my_list)

print('------------------')
my_list.insert(3, -10000000)
print(my_list)

print('------------------')
my_list.pop(2)
print(my_list)

print('------------------')
my_list.remove(-39)
print(my_list)
print('--------------------------------------------------')

new_list = ['loop', None,'start', None]

my_list.extend(new_list)
print(my_list)

print('------------------')

print(my_list.index(568))

res = None

try:
    my_list.index(None)
    for elem in range(len(my_list)):
        res = my_list.index(None)
        my_list.pop(res)
except ValueError:
    print('No Value in list')
finally:
    print(res)
    print(my_list)

print('------------------')

my_list = [1,5,2,7,1,4,5]
sorted_list = sorted(my_list.copy())
print(sorted_list)

my_list = [1,5,2,7,1,4,5]
sorted_list.sort()
print(sorted_list)

my_list = [1,5,2,7,1,4,5]
sorted_list.sort(reverse=False)
print(sorted_list)

my_list = [1,5,2,7,1,4,5]
sorted_list.sort(reverse=True)
print(sorted_list)

print('------------------')

my_list = list()
user_input = int(input('Enter value (0 - exit): '))
while user_input != 0:

    if user_input not in my_list:
        my_list.append(user_input)
    user_input = int(input('Enter value (0 - exit): '))

print(my_list)

print('------------------')


