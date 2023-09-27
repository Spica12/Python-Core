class User:

    def __init__(self, name: str, age: int|str) -> None:
        self.__private_name = None
        self.__private_age = None
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self.__private_name
    
    @name.setter
    def name(self, value: str) -> None|Exception:
        if value.isalpha():
            self.__private_name = value
        else:
            raise Exception('Wrong name')
        
    @property
    def age(self) -> int:
        return self.__private_age
    
    @age.setter
    def age(self, value: str) -> None|Exception:
        if int(value) >= 18:
            self.__private_age = value
        else:
            raise Exception('Wrong age')


user_1 = User('Bob', '26')
(print(user_1.name, user_1.age))    # Bob 26

user_2 = User('123', 22)
