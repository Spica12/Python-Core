"""
__init__

Відповідає за ініціалізацію об'єкта. Коли ви створюєте об'єкт класу, 
то спочатку створюється порожній об'єкт, який містить лише обов'язкові 
службові атрибути. Після цього (об'єкт вже створено) автоматично 
викликається метод __init__, який ви можете модифікувати під ваші потреби.

Зверніть увагу, що метод __init__ може приймати аргументи позиційні та/або 
іменні, як і будь-який інший метод. Коли ми створюємо об'єкт класу Human, 
ми повинні класу передати обов'язково хоча б один аргумент, оскільки 
метод __init__ повинен приймати обов'язково name.
"""

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'
    

bill = Human('Bill')
print(bill.say_hello())     # Hello! I am Bill
print(bill.age)             # 0

jill = Human('Jill', 20)
print(jill.say_hello())     # Hello! I am Jill
print(jill.age)             # 20