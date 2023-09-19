class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age





person = Person('Oleh', '22')
person.__dict__['age'] = 'old'
print(person.age)     # 22

person.age = 10

print(person.age)     # 10

print(person.age, person.__dict__)     # 10 {'_Person__name': 'Oleh', '_Person__age': 10}
