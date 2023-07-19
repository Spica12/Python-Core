print('----------- Example 1 ----------')

def print_max(a, b):

    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equal', b)
    else:
        print(b, 'max')

print_max(3, 4) # Пряма передача значень
print_max(3, 3) 
print_max(6, 3) 



x = 5
y = 7

print_max(x, y) # Передача змінних у якості аргументів.

print('----------- Example  ----------')