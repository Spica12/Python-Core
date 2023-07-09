import math # Для роботи з числами
#import сmath # Для роботи з комплексними числами

# Щоб знайти КВАДРАТНИЙ КОРІНЬ із числа, треба використати метод
a = math.sqrt(100) # 10
print(a)
print()

# -----------------------------------
#Рішення квадратного рівняння
a = -2
b = 7
c = -6
D = (b ** 2) - (4 * a * c)
x1 = (-b + math.sqrt(D))/(2 * a)
x2 = (-b - math.sqrt(D))/(2 * a)
print('a*x^2 + b*x^2 + c = 0')
print(f"a = {a}, b = {b}, c = {c}")
print(f"D = {D}")
print(f"x1 = {x1}, x2 = {x2}")
print()
# ------------------------------------

alpha_deg = 30
alpha_radians = math.radians(alpha_deg)
print(alpha_deg, alpha_radians)

arccos_alpha = math.acos(alpha_radians)
print(arccos_alpha)

sin_alpha = math.sin(alpha_radians)
print(sin_alpha)

cos_alpha = math.cos(alpha_radians)
print(cos_alpha)

print()


