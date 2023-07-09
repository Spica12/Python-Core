a = True
b = False

age = 18
adult1 = age >= 18  #True
print(adult1)

age = 15
adult1 = age >= 18  #False
print(adult1)

a = 3
b = 5

# ---------------------------------------------
# | Оператор відношення |      Значення       |
# ---------------------------------------------
# |          <          | Менше               |
# |          <=         | Менше або дорівнює  |
# |          >          | Більше              |
# |          >=         | Більше або дорівнює |
# |          ==         | Дорівнює            |
# |          !=         | Не дорівнює         |
# ---------------------------------------------
# Більше
c = a > b
print(f'c = {c}')   #False

# Менше
d = a < b
print(f'd = {d}')   #True

# Дорівнює
e = a == b
print(f'e = {e}')   #False

# Не дорівнює
f = a != b
print(f'f = {f}')   #True

is_active = True
is_delete = False

# Типи даних
name = 'Vitalii'
age = 33
is_active = True
subscription = None

# --------------------------
# Функція bool()
a = 3
b = bool(a)
print(b) # True

c = 0
d = bool(c)
print(d) # False

e = ''
f = bool(e)
print(f) # False

g = 'Vitalii'
h = bool(g)
print(h) # True
# ----------------------------
