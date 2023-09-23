"""
Створіть клас NumberString, успадкуйте його від класу UserString, 
визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
--------------------------------------------------------------------
from collections import UserString


class NumberString(UserString):
    def number_count(self):
        
"""
from collections import UserString



class NumberString(UserString):

    def __init__(self, string):
        self.string = string

    def number_count(self):
        return len(list(filter(lambda char: char.isdigit(), self.string)))