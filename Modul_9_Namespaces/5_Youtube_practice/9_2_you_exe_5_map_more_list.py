list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']


for n in map(lambda x, y: f'{y}: {x}', list_1, list_2):
    print(n)

# a: 1
# b: 2
# c: 3
# d: 4
# e: 5


list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd', 'e']

print(f'{len(list_1) = }')
print(f'{len(list_2) = }')

for n in map(lambda x, y: f'{y}: {x}', list_1, list_2):
    print(n)

# len(list_1) = 4
# len(list_2) = 5
# a: 1
# b: 2
# c: 3
# d: 4