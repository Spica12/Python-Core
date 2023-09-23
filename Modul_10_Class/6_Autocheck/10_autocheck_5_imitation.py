"""
Створіть клас Cat, батьківським класом якого є клас Animal. У класі Cat 
виконайте перевизначення методу say, щоб він повертав рядок "Meow" для 
екземплярів класу Cat.

Фактично ми виконуємо при цьому поліморфізм. Поліморфізм - це здатність 
програми вибирати різні реалізації при виклику операцій з однією і тією 
ж назвою. Тобто при виклику методу say в екземпляра класу Cat викликається
 нова реалізація, а не успадкована від класу Animal

Створіть також змінну cat, яка буде екземпляром класу Cat. При створенні 
змінної cat ім'я кота має бути "Simon", а вага - 10 одиниць.
-----------------------------------------------------------------------
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):

    def say(self):
        return "Meow"
    
cat = Cat('Simon', 10)