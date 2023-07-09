print('------------Приклад 1------------------------')
# Для виділення блоку інструкцій треба використовувати 4 пробіли.
# Використовувати табуляцію не рекомендується
# Використовувати табуляцію та пробіли важається помилкою

x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))

result = y / x
print(result)

print('------------Приклад 2------------------------')
x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))
    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))
        if x == 0:
            print("X can't be equal to zero")
            x = int(input('X: '))

result = y / x
print(result)

print('------------Приклад 3------------------------')
x = int(input('X: '))
y = int(input('Y: '))

if x >= 0:
    if y >= 0: # x > 0, y > 0
        print('Перша чверть')
    else: # x > 0, y < 0
        print('Четверта чверть')
else:
    if y >= 0: # x < 0, y > 0
        print('Друга чверть')
    else: # x < 0, y < 0
        print('Третя чверть')