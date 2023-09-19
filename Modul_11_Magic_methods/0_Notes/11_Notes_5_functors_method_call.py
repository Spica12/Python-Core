"""
__call__

Функтори — це об'єкти, які поводяться як функції у тому сенсі, що 
їх можна викликати та передавати їм аргументи. 

Функція у Python — це такий самий об'єкт, але у ньому реалізований 
метод __call__, який відповідає за синтаксис виклику з круглими дужками.

"""

class Adder:

    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value
    

two_adder = Adder(2)
print(two_adder(5))     # 7
print(two_adder(4))     # 6

three_adder = Adder(3)
print(two_adder(5))     # 8
print(two_adder(4))     # 7
