import math

a = -2
b = 7
c = -6
D = (b ** 2) - (4 * a * c)
x1 = (-b + math.sqrt(D))/(2 * a)
x2 = (-b - math.sqrt(D))/(2 * a)

print('D = ', D)
print('x1 = ', x1)
print('x2 = ', x2)