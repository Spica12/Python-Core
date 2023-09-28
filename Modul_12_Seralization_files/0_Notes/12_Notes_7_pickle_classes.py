"""
Робота з класами користувача

Ви можете зберігати об'єкти для подальшого використання, але з умовою. 
Самі класи та функції pickle зберігати не вміє і, якщо вам потрібно 
розпакувати упакований об'єкт класу, то сам клас повинен бути оголошений раніше у коді.
"""

import pickle

class Human:

    def __init__(self, name: str) -> None:
        self.name: str = name


bob = Human('Bob')

# Серелізація екземпляру класу
encoded_bob = pickle.dumps(bob)

# Десерелізація екземпляру класу
decoded_bob = pickle.loads(encoded_bob)

print(bob.name == decoded_bob.name) # True
print(bob)                          # <__main__.Human object at 0x000002470B0BEF10>
print(decoded_bob)                  # <__main__.Human object at 0x000002470B0BF890>
print(bob is decoded_bob)           # False



