
#  class <name>:
#       pass


class User:

    name = None
    age = None
    phone = None

    def greeting(self):
        return f'Hello! I am {self.name} my self {self}'
    

user_1 = User()

print(user_1)       # <__main__.User object at 0x000001A5CACEEF10>

user_1.name = 'Vlad'
user_1.age = 25
user_1.phone = '234567890 '

print(user_1.name, user_1.age, user_1.phone)    # Vlad 25 234567890 
print(user_1.greeting())                        # Hello! I am Vlad my self <__main__.User object at 0x0000021929CAEED0>
print(user_1)                                   # <__main__.User object at 0x0000021929CAEED0>




