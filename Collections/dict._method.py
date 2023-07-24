#                                            pop(keys)
# Повернути значення елементу та 
# видалити його зі списку  
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')

print(chars) # {'a': 1}
print(b_num) # 2




#                                            update(another_dict)
# Розширює словник значенням іншого словника
chars = {'a': 1, 'b': 2}
chars.update({'c': 3})

print(chars) # {'a': 1, 'b': 2, 'c': 3}




#                                            clear()
# Очищає словник не створюючи нового
chars = {'a': 1, 'b': 2}
chars.clear()

print(chars) # {}




#                                            copy()
# Повертає копію словника
chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()

print(chars) # {'a': 1, 'b': 2}
print(chars_copy) # {'a': 1, 'b': 2}
print(chars_copy == chars) # True




#                                            get(key[, default])
# Не виклакає виключення, якщо ключа немає
# в словнику, повертає default, за замовчуванням
# default=None
chars = {'a': 1, 'b': 2}
c_idx = chars.get('c', -1)
b_idx = chars.get('b', -1)

print(c_idx) # -1
print(b_idx) # 2




#                                           items()

# Використовується дл яповернення і ключа і значення
lang = {'Python': 1991, 'Java': 1195, 'JS': 1995}

for l, value in lang.items():
    print(f'Programming language {l} - released {value}')






#                                                   in
user = {
    'name': 'Bill',
    'surname': 'Bosh',
    'age': 22
}

if "age" in user:
    print(f'User is {user["age"]} years old.')

print('age' in user) # True
print('email' in user) # False

# Якщо є запис то його можна змінити,
# Якщо запису нема, то він створиться
lang = {'Python': 1991,
        'Java': 1995
}
lang['Java'] = 1991
lang['JS'] = 1995

print(lang)



# Можна створити список користувачів, в якому кожен
# елемент є словнико з інформацією про користувача
user_1 = {'name': 'Jane', 'age': 21}
user_2 = {'name': 'Moris', 'age': 23}
user_3 = {'name': 'Steve', 'age': 24}

persons = [user_1, user_2, user_3]

for user in persons:
    for field in user:
        print(user.get(field))
# Jane
# 21
# Moris
# 23
# Steve
# 24





