person = {'name': 'Vitalii', 'age': 22}

copy_person = person.copy()

print(person.get('name', 'Noname'))
print(person.get('age', 'Noname'))

print('-----------------------------')

person.update({'secret': [1, 2, 3, 4, 5]})

print(person)

dict_a = {'alex': 12, 'Olga': 10}
dict_b = {'boris': 12, 'Kostya': 10}
dict_c = {'Ira': 12, 'Vova': 10}

dict_united = dict()
for value in (dict_a, dict_b, dict_c):
    dict_united.update(value)

print(dict_united)