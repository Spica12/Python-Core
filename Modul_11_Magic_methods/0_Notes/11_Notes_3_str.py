"""
__str__

Відповідає за те, як об'єкт конвертується в рядок.

Коли ви викликаєте функцію str та передаєте їй якийсь об'єкт, то насправді 
цей об'єкт викликається методом __str__.
"""

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello! I am {self.name}. I am {self.age} years old.'
    
bill = Human('Bill', 15)
bill_str = str(bill)
print(bill_str)         # Hello! I am Bill. I am 15 years old.
