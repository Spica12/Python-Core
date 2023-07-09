print('------------Приклад 1------------------------')
# Тернарні операції
# Повертають залежно від того чи є умова істиною або брехнею
is_nice = True
state = 'nice' if is_nice else 'not nice'
print('State: ', state)

print('------------Приклад 2------------------------')
#  Короткий варіант тернарного оператора
#  Треба використовувати оператор OR
some_data = None
msg = some_data or 'Не було повернуто даних'
print(msg)

print('------------Приклад 3------------------------')
is_access = False
message = 'Welcome' if is_access else 'Forbidden'
print(message)

print('------------Приклад 4------------------------')
some_data = None
message = some_data or 'Not data'
print(message)