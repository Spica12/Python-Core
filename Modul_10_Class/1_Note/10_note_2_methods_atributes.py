
class User:

    name = 'UserName'
    age = 15


    def say_name(self):
        print(f'Hi! I am {self.name} and I am {self.age} years old')


    def set_age(self, age):
        self.age = age


bob = User()
bob.name = 'Bob'

bob.say_name()      # Hi! I am Bob and I am 15 years old

bob.set_age(25)
bob.say_name()      # Hi! I am Bob and I am 25 years old