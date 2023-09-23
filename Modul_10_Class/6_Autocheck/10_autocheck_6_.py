"""
Створіть клас Dog, батьківським класом якого є клас Animal. У класі Dog 
виконайте перевизначення методу say, щоб він повертав рядок "Woof" для 
екземплярів класу Dog.

У конструкторі класу Dog введіть нову властивість breed - порода, при 
цьому повинні залишитись всі властивості, успадковані від класу Animal.

Створіть у коді наступний екземпляр класу Dog.

dog = Dog("Barbos", 23, "labrador")
--------------------------------------------------
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog():
"""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):

    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return f'Woof'
    

dog = Dog("Barbos", 23, "labrador")
    