from datetime import datetime

test = datetime = datetime.now()
print(str(test))    # 2023-09-19 19:57:01.656771
print(repr(test))   # datetime.datetime(2023, 9, 19, 19, 57, 1, 656771)

# str   - для зручного виведення відображення
# repr  - для отримання повної інформації про об'єкт для розробника

test_2 = '1234'

print(str(test_2))    # 1234
print(repr(test_2))   # '1234'

test_3 = [1, 2, 3]

print(str(test_3))    # [1, 2, 3]
print(repr(test_3))   # [1, 2, 3]

# Об'єкт який змінюється, то відображення однакове. бо можна змінити
