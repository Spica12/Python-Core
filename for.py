# Використовуэться для перебору усІх елементів контейнерів
# Наприклад, списків
# Цикл буде виконуватись скільки елекментів в списку.

print('------------Приклад 1------------------------')
fruit = 'apple'
for char in fruit:
    print(char)
# a
# p
# p
# l
# e

print('------------Приклад 2------------------------')
for i in range(0, 10):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
print('------------Приклад 3------------------------')
num = 10

for variable in range(num):
    if variable % 2 == 1:
        continue
    print(variable)
# 0
# 2
# 4
# 6
# 8