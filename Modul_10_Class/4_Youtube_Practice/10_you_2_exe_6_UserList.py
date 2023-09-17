from collections import UserDict, UserList, UserString
from random import randint


class MyList(UserList):

    def append(self):
        print('No element for you')

    def say_hello(self):
        print(f'Hello from {self.data}')

    def update_with_random(self):
        self.data[0] = randint(0, 10)


a = MyList('asdfasdf')
a.update_with_random()
a.say_hello()