#  Цикл while

# Дозволяє виконати інструкції, доки виконується умова
# що вказана в циклі

print('------------Приклад 1------------------------')
a = 1
while a <= 5:
    print (a)
    a = a + 1

# 1
# 2
# 3
# 4
# 5

print('------------Приклад 2------------------------')
# Команда break

# Зупиняє цикл в момент виклику і не завершує ітерацію

a = 0
while True:
    print(a)
    if a >= 5:
        break
    a = a + 1

# 0
# 1
# 2
# 3
# 4
# 5

print('------------Приклад 3------------------------')
while True:
    user_input = input('exit для виходи ')
    print(user_input)
    if user_input == 'exit':
        print('Stop program')
        break

print('------------Приклад 4------------------------')
# Команда continue

# Викликає наступну ітерацію, без завершення поточної
# Вирази, що залишились, будуть не виконані

a = 0 
while a < 6:
    a = a + 1
    if not a % 2: # увага, що not
        continue
    print(a)

# ---------------------
# | a % 2 | not a % 2 |
# ---------------------
# |   2   |     1     |
# |   4   |     3     |
# |   6   |     5     |
# ---------------------

print('------------Приклад 5------------------------')
# Команда break та continue 

# Прериваю ть тільки свій цикл і не впливають на інші.

while True:
    number = input('number (0 to exit) = ')
    number = int(number)
    if number == 0:
        break
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break
    

print('------------Приклад 6------------------------')
num = int(input('Введіть ціле число від 1 до 10: '))
count = 10 - num
i = 1
while i <= count:
    print(f'Ітерація {i}')
    i = i + 1
print('Програма закінчена')

print('------------Приклад 7------------------------')
count = 0
text = 'Hello world!'
while count <= (len(text) - 1):
    print(text[count])
    count +=1
# H
# e
# l
# l
# o
# 
# w
# o
# r
# l
# d
# !
