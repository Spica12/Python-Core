"""
Качина типізація — це механізм властивий Python, який дозволяє 
використовувати будь-які об'єкти один замість іншого, аби в обох 
були потрібні методи та поля. Качиною ця типізація називається 
від приказки: 

"Якщо крякає як качка, плаває як качка і літає як качка, — це качка". 

Це добре відображає суть підходу, реалізованого у Python. 
Ні, інтерпретатор не перевіряє, що у функцію або метод був переданий 
об'єкт потрібного або дочірнього класу, достатньо щоб в об'єкта 
були потрібні методи і все буде працювати.
"""

class Mammal:
    phrase = ''
    def voice(self):
        return self.phrase
    

class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whoooooooo!!!!'
    

class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)                # Recorded "Meow!"
r.record_animal(dog)                # Recorded "Bark!"
r.record_animal(strange_animal)     # Recorded "Whoooooooo!!!!"