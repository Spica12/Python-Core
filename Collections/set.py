# Множини (set)

empty = set()
print(empty)            # set()

a = set('Hello')
print(a)            # {'e', 'H', 'l', 'o'}

b = {1, 2, 3, 4, 5, 5 , 5, 10, 4, 3,}
print(b)            # {1, 2, 3, 4, 5, 10}

list_set = set(['My', 'set'])
print(list_set) # {'My', 'set'}

#                                                    in
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_prime = 3 in prime_numbers

print(is_prime) # True

#                                                    len
b = {1, 2, 3, 4, 5, 5 , 5, 10, 4, 3,}

print('len b:', len(b), b) # len b:  6 {1, 2, 3, 4, 5, 10}

#                                                    for
b = {1, 2, 3, 4, 5, 5 , 5, 10, 4, 3,}

for i in b:
    print(i)
# 1
# 2
# 3
# 4
# 5
# 10
