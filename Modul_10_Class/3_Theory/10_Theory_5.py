

class Animal:

    def __init__(self, nickname, age):

        self.nickname = nickname
        self.age = age


class Cat(Animal):

    def __init__(self, nickname, age, owner):
        super().__init__(nickname, age)
        self.owner = owner

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
    

class Owner:

    def __init__(self, name, phone):

        self.name = name
        self.phone = phone

    def info(self):
        return f'{self.name} : {self.phone}'
    


owner = Owner('Oleg', '1234566')
cat = Cat('Alex', 4, owner)

print(cat.owner.info())     # Oleg : 1234566

