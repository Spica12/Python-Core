

class Animal:

    go_over = 0

    def __init__(self, nickname, age):

        self.nickname = nickname
        self.age = age

    
    def step_count(self):
        self.go_over += 1000


class Cat(Animal):

    def __init__(self, nickname, age):
        super().__init__(nickname, age)

    def sound(self):
        return 'Meow'
    
    def get_info(self):
        return f'Cat name is {self.nickname} and It\'s {self.age}'
    


class Dog(Animal):

    def __init__(self, nickname, age):
        super().__init__(nickname, age)

    def sound(self):
        return 'Bark!'
    
    def get_info(self):
        return f'Dog name is {self.nickname} and It\'s {self.age}'
    




cat = Cat('Alex', 3)
dog = Dog('Garik', 2)

print(cat.get_info())
print(cat.age)
print(cat.sound())

for item in (cat, dog):
    print(item.get_info())
    print(item.sound())


print(isinstance(cat, Cat))     # True
print(isinstance(dog, Cat))     # False
print(isinstance(cat, Animal))  # True

print(super(Dog, dog).get_info())





