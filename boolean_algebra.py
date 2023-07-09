print('------------Приклад 1------------------------')
name = 'Taras'
age = 22
has_driver_licence = False

if name and age >= 18 and has_driver_licence:
    print(f'User {name} can rent a car')
else:
    print(f"User {name} can't rent a car")
print('------------Приклад 2------------------------')
#           and
#----------------------------
#|   A   |   B   | A and B  |
#----------------------------
#| True  | True  |   True   |
#----------------------------
#| True  | True  |  False   |
#----------------------------
#| False | True  |  False   |
#----------------------------
#| False | False |  False   |
#----------------------------

a = True and False
print('and: ', a)

print('------------Приклад 3------------------------')
#           or
#----------------------------
#|   A   |   B   | A and B  |
#----------------------------
#| True  | True  |   True   |
#----------------------------
#| True  | False |   True   |
#----------------------------
#| False | True  |   True   |
#----------------------------
#| False | False |  False   |
#----------------------------

a = True or False
print('or: ', a)

print('------------Приклад 4------------------------')
#           not
#-----------------
#|   A   | not A | 
#-----------------
#| True  | False | 
#-----------------
#| False | True  |  
#-----------------

a = not 2 < 0 # True
print('not: ', a)

