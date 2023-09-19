"""
__iter__
__next__

Протокол ітератора у Python реалізований за допомогою методу __iter__. 

Цей метод повинен повертати ітератор. Ітератором може бути будь-який 
об'єкт, у якого є метод __next__, який за кожного виклику повертає 
значення. Щоб створити ітератор, достатньо реалізувати метод __next__.
"""

class Iterable:

    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration
    

class CustomIterator:
    def __iter__(self):
        return Iterable()
    

c = CustomIterator()

for i in c:
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10