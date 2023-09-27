class User:
    name = None
    last_name = None


user_1 = User()
user_1.name = 'Boris'
user_1.last_name = 'Johnson'
print(user_1.name, user_1.last_name)    # Boris Johnson







class User:
    
    def __init__(self, name: str, last_name: str=None) -> None:
        self.name = name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'Full name: {self.name} {self.last_name}'
    
    def __repr__(self) -> str:
        return f'User({self.name}, {self.last_name})'


user_2 = User('Boris', 'Johnson')
print(user_2.name, user_2.last_name)    # Boris Johnson
print(user_2)   # <__main__.User object at 0x0000018C6F8FF290>   
print(f'Full name: {user_2.name} {user_2.last_name}')   # Full name: Boris Johnson

print(user_2)   # Full name: Boris Johnson   

user_3 = User('Bob', 'Johnson')

users = []
users.append(user_2)
users.append(user_3)
print(users)            # [User(Boris, Johnson), User(Bob, Johnson)]



