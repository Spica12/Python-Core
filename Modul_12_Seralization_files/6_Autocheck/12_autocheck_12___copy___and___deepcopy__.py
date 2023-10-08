"""
Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.

---------------------------------------------------------------------------

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        
            
            
            
            
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        
        

    def __deepcopy__(self, memo):
"""

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):

        copy_obj = Person(self.name, self.email, self.phone, self.favorite)

        return copy_obj

    
    def __str__(self):
        return f'Person({self.name}, {self.email}, {self.phone}, {self.favorite})'
    
    def __eq__(self, value):
        return self.name == value.name and self.email == value.email and self.phone == value.phone and self.favorite == value.favorite
    
            
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename)
        copy_obj.__dict__ = copy.copy(self.__dict__)

        return copy_obj
        

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename)
        memo[id(self)] = copy_obj
        copy_obj.contacts = copy.deepcopy(self.contacts, memo)
        copy_obj.is_unpacking = False
        copy_obj.count_save = 0

        return copy_obj


person_1 = Person('Bob', 'bob@gmail.com', '123', True)
person_2 = Person('John', 'john@gmail.com', '456', False)
person_3 = Person('Mark', 'mark@gmail.com', '789', True)


filename = 'D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\6_Autocheck\\12_autocheck_12___copy___and___deepcopy__.py'
contacts = Contacts(filename, [person_1, person_2, person_3])

copy_object = copy.copy(contacts)
print('Copy')
print(contacts.contacts[0])
print(contacts.contacts[1])
print(contacts.contacts[2])
print()


print(copy_object.contacts[0])
print(copy_object.contacts[1])
print(copy_object.contacts[2])
print()

print(contacts.contacts[0] == copy_object.contacts[0])
print(contacts.contacts[1] == copy_object.contacts[1])
print(contacts.contacts[2] == copy_object.contacts[2])
print()

print(contacts.contacts[0] is copy_object.contacts[0])
print(contacts.contacts[1] is copy_object.contacts[1])
print(contacts.contacts[2] is copy_object.contacts[2])



deepcopy_contacts = copy.deepcopy(contacts)
print('Deepcopy')
print(f'{contacts.contacts}')
print(f'{deepcopy_contacts.contacts}')

print(contacts.contacts[0])
print(contacts.contacts[1])
print(contacts.contacts[2])
print()


print(deepcopy_contacts.contacts[0])
print(deepcopy_contacts.contacts[1])
print(deepcopy_contacts.contacts[2])
print()

print(contacts.contacts[0] == deepcopy_contacts.contacts[0])
print(contacts.contacts[1] == deepcopy_contacts.contacts[1])
print(contacts.contacts[2] == deepcopy_contacts.contacts[2])
print()

print(contacts.contacts[0] is deepcopy_contacts.contacts[0])
print(contacts.contacts[1] is deepcopy_contacts.contacts[1])
print(contacts.contacts[2] is deepcopy_contacts.contacts[2])



