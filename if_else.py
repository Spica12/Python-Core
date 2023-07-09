print('------------Приклад 1------------------------')
age = 33 #input('How old are you? ')

if int(age) >= 18:
    print('You are adult already.')
else:
    print('You are infant yet.')
print('------------Приклад 2------------------------')
# 
a = 4 #input('Введіть число: ')
a = int(a)

if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')
print('------------Приклад 3------------------------')
# Перевіряє умови, умова виконується, виходить з перевірки умов
# Тобто всі інші умови ігноруються
a = 1 #input('Введіть число: ')
a = int(a)

if a > 0:
    print('Число додатне')
elif a == 1: #Умова ніколи не буде виконана, бо а > 0 викон
    print("Число дорівнює 1")
else:
    print('a <= 0')
print('------------Приклад 4------------------------')
# Число 0 приводиться до False (ціле, дробове або комплексне)
# Всі інші приводяться до True
money = 0
if money:
    print(f'You have {money} on your bank acoount')
else:
    print('Yoy have no money and no debts')
print('------------Приклад 5------------------------')
# None приводиться до False
# Всі інші приводяться до True
result = None
if result:
    print(result)
else:
    print('Result is None, do something')
print('------------Приклад 5------------------------')
# Порожній контейнер, рядок приводиться до False
# Всі інші приводяться до True
user_name = ''
if user_name:
    print(f'Hello {user_name}!')
else:
    print('Hi, Anonym!')