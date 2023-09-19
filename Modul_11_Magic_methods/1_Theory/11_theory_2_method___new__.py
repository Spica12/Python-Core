# __new__ - створює об'єкт класу, а метод __init__ - ініцілюазивути
#  добавляється перед __init__

class Foo:

    def __new__(cls, *args, **rwargs):
        print('Static method')
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value=None):
        print('Call constructor')
        self.value = value


test = Foo(15)
print(test.value)       # 15