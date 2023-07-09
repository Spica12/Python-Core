 
# Минулого разу ми просто вказали значення коефіцієнтів a, b, c. 
# Тепер, коли ми вже знаємо про розгалуження, ми можемо перевіряти 
# значення дискримінанта і, в залежності від того додатне чи від'ємне, 
# провести розрахунок коренів. Виконайте розрахунок коренів для 
# довільних значень коефіцієнтів a, b, c.
# ----------------------------------------
# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c

# if
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#  --------------------------------------

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x = (-b) / (2 * a)
else:
    print('дійсних коренів немає')