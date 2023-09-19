class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)



person = Person('Oleh', '22')

print(person.get_age())     # 22

person.set_age(5)

print(person.get_age())     # 5

person.age = 10

print(person.age)     # 10


