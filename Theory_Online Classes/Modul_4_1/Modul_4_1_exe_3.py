my_set = set('hi there, HI!')

print(my_set)

# 12373427354 = 'i'
# 27348624234 = ' '

print('---------------------------')

my_set = {4, 6, 'sam', 'python', 100}

my_set.add('test')
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard('test')
print(my_set)

list_fata_one = [1, 1, 3, 6, 7, 9, 0, 34, 76, 894, 90, 34]
list_fata_two = [1, 2, 3, 5, 7, 78, 34, 34, 76, 894, 90, 34]

print(list(set(list_fata_one) & set(list_fata_two)))
print(list(set(list_fata_one) - set(list_fata_two)))

list_fata_one = [1, 1, 3, 6, 7, 9, 0, 34, 76, 894, 90, 34, 7]
list_fata_two = [1, 2, 4, 6]

def unique(data):
    return len(data) == len(set(data))

print(unique(list_fata_one))
print(unique(list_fata_two))