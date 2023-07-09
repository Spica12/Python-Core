# Приведення до bool()
# 1 - Число 0 приводиться до False
# 2 - Значення None приводиться до False
# 3 - '' (порожній рядок) приводиться до False
# 4 - Решта випадків приводиться до True

# Завдання:
# У нас є три логічні змінні.

# - Перша визначає статус користувача is_active, яка дорівнює True
#   або False.
# - Друга is_admin визначає, чи є у користувача права адміністратора 
#   теж булевого типу.
# - Третя is_permission — чи дозволено доступ, теж булевого типу.

# 1. Приведіть змінні is_active, is_admin та is_permission до булевого 
#    вигляду.
# 2. Надайте змінній access значення, яке покаже, чи є доступ у користувача.
#    Використовуйте логічні оператори.
# 3. Адміністратор завжди має доступ, незалежно від значень змінних 
#    is_permission та is_active.
# 4. Користувач має доступ, тільки якщо is_permission дорівнює True 
#    та is_active також дорівнює True.

is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

access = is_admin or is_active and is_permission
print(access)