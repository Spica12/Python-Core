from copy import copy, deepcopy

class Users:

    def __init__(self) -> None:
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def __copy__(self):
        copy_self = Users()
        copy_self.user_list = copy(self.user_list)

        return copy_self


class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

user_1 = User('Jack', 19)
user_2 = User('Jogn', 20)

users = Users()
users.add_user(user_1)
users.add_user(user_2)

copy_users = copy(users)

print(users.user_list)
print(copy_users.user_list)


user_2 = User('Biba', 20)
user_3 = User('Bob', 18)
copy_users.add_user(user_3)

print(users.user_list)
print(copy_users.user_list)

