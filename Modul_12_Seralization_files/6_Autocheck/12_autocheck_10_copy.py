"""
Для копіювання екземпляра класу Person із попереднього прикладу реалізуйте 
функцію copy_class_person. Як параметр вона приймає екземпляр класу person, 
та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.

Приклад коду:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True

-----------------------------------------------------------------------------------

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
"""
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    # attributes = copy.copy(person.__dict__)
    # copy_name = attributes['name']
    # copy_email = attributes['email']
    # copy_phone = attributes['phone']
    # copy_favorite = attributes['favorite']

    # return Person(copy_name, copy_email, copy_phone, copy_favorite)
    return copy.copy(person)