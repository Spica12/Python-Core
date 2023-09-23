"""
Для минулого завдання додамо клас Owner — власника собаки. У класу є три 
атрибути: ім'я — name, вік — age та адреса — address. Також необхідно 
реалізувати метод info, який повертає словник з ключами 'name', 'age' і 
'address', та значення яких дорівнюють відповідним властивостям екземпляра класу.

Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. 
Додати до класу Dog метод who_is_owner, який повертає результат виклику методу 
info екземпляра класу Owner, тобто це словник з ключами name, age та address власника.
--------------------------------------------------------------------------------
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, ):
        
        
        

    def info(self):
        
            
            
            
        


class Dog(Animal):
    def __init__(self, nickname, weight, breed, ):
        self.breed = breed
        
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
"""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            'name': self.name,
            'age' : self.age,
            'address': self.address
        }
        
        
class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()