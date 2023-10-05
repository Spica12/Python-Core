from copy import copy

class Car:

    def __init__(self, brand, model, color) -> None:
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return ' '.join([f'{k}: {v}' for k, v in self.__dict__.items()])


car1 = Car('Tesla', 'Model X', 'red')
car2 = copy(car1)

car2.color = 'black'

print(car1)