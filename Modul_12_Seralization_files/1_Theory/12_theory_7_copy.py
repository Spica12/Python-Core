from copy import copy, deepcopy

lst1 = [1, 2, 3]
lst2 = lst1

lst2[1] = 10

print(lst1)     # [1, 10, 3]

print('-----------------------')

lst1 = [1, 2, 3, [1, 2, 3]]
lst2 = lst1[:]

lst2[3][1] = 10

print(lst1)     # [1, 2, 3, [1, 10, 3]]

print('-----------------------')

lst1 = [1, 2, 3]
lst2 = copy(lst1)

lst2[1] = 10

print(f'{lst1 = }, {lst2 = }')     # lst1 = [1, 2, 3], lst2 = [1, 10, 3]

print('-----------------------')

lst1 = [1, 2, 3, [10, 12, 13]]
lst2 = copy(lst1)

lst2[3][0] = 100

print(f'{lst1 = }, {lst2 = }')     # lst1 = [1, 2, 3, [100, 12, 13]], lst2 = [1, 2, 3, [100, 12, 13]]


print('-----------------------')

lst1 = [1, 2, 3, [10, 12, 13]]
lst2 = deepcopy(lst1)

lst2[3][0] = 100

print(f'{lst1 = }, {lst2 = }')     # lst1 = [1, 2, 3, [10, 12, 13]], lst2 = [1, 2, 3, [100, 12, 13]]


