
"""
У Python неможливо інкапсулювати (зробити недоступними) атрибути класу. 
Ви завжди можете отримати доступ до будь-якого атрибуту. Щоб якось 
вказати розробнику, що доступ до атрибута напряму небажаний, прийнято 
називати такі поля або методи, починаючи з одного нижнього підкреслення. 
Якщо ж назвати атрибут так, що спочатку буде два нижні підкреслення, то 
включиться механізм "приховування" імен. Це не означає, що доступ до 
цього поля буде закрито, просто дещо ускладнений.
"""

class Secret:
    public_field = 'This is public'
    _private_field = 'Avoid using this please'
    __real_secret = 'I am hidden'

s = Secret()

print(s.public_field)           # This is public
print(s._private_field)         # Avoid using this please
print(s._Secret__real_secret)   # I am hidden


class PositiveNumber:

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()

p.value = 1
print(p.value)  # 1

p.value = -1    # Only numbers greater zero accepted

p._PositiveNumber__value = -1   # -1
print(p.value)
