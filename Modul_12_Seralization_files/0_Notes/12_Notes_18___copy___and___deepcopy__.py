"""
Ще одна проблема вирішується за допомогою пакету copy — це копіювання 
об'єктів користувача. Щоб створити об'єкт, який буде коректно оброблятися 
функціями copy та deepcopy, ваш клас повинен реалізувати два магічних методи: 

__copy__ та __deepcopy__ для поверхневого та глибокого копіювання відповідно.
"""

from copy import copy, deepcopy

class Expenses:

    def __init__(self) -> None:
        self.data = dict()
        self.places = list()

    def spent(self, place: str, value: int) -> None:
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self) -> object:
        copy_obj = Expenses()
        copy_obj.data = self.data
        copy_obj.places = self.places

        return copy_obj
    
    def __deepcopy__(self, memo: dict):
        copy_obj = Expenses()
        memo[id(self)] = copy_obj
        copy_obj.data = deepcopy(self.data, memo)
        copy_obj.places = deepcopy(self.places, memo)

        return copy_obj
    

e = Expenses()
e.spent('hotel', 100)
e.spent('taxi', 10)
print(e.places, e.data, '', sep='\n')

e_copy = copy(e)
print(e_copy is e)
e_copy.spent('bar', 30)
print(e.places, e.data, '', sep='\n')

e_deep_copy = deepcopy(e)
print(e_deep_copy is e)
e_deep_copy.spent('airport', 400)
print(e_deep_copy.places, e_deep_copy.data, '', sep='\n')
