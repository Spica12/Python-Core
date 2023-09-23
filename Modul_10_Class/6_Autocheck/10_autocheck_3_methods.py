"""
Для попереднього завдання реалізуйте в класі Animal метод change_weight, 
який має змінювати вагу тварини.

Викличте функцію change_weight(12) для об'єкта animal та змініть значення 
початкової ваги з 10 на 12 одиниць.
---------------------------------------------
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    
        


animal = Animal("Simon", 10)
"""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    
        


animal = Animal("Simon", 10)
animal.change_weight(12)
print(animal.weight)    # 12