

class Animal:

    go_over = 0

    def __init__(self, nickname, age):

        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f'Animal name is {self.nickname} and It\'s {self.age}'
    
    def step_count(self):
        self.go_over += 1000


class Cat(Animal):

    def __init__(self, nickname, age):
        super().__init__(nickname, age)

    def sound(self):
        return 'Meow'


cat = Cat('Alex', 3)

print(cat.get_info())
print(cat.age)
print(cat.sound())






