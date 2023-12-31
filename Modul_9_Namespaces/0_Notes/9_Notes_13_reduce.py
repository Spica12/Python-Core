from functools import reduce

# Приймає ітератор для обробки, але сама не є ітератором і повертає єдиний результат.

# Функція reduce застосовує функцію з двома параметрами кумулятивно до елементів, 
# що підлягають ітерації, необов'язково починаючи з початкового аргументу. 

# Має наступний синтаксис:
#                           reduce(func, iterable[, initial])

# де, func - це функція, до якої кумулятивно застосовується кожен елемент iterable
#     initial -  необов'язкове значення, яке поміщається перед елементами обчислення, 
#                що ітерується, і служить значенням за замовчуванням, коли об'єкт, що 
#                ітерується, порожній.

result = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(result)   # 24

# 1 * 2 = 2
#         2 * 3 = 6
#                 6 * 4 = 24

result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)
print(result)   # 72

# 1 * 2 = 2
#         2 * 3 = 6
#                 6 * 4 = 24
#                         24 * 3 = 72 , де 3 це initial