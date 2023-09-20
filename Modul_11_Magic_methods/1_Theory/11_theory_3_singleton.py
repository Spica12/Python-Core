
class SingelTon(object):
    __instance = None

    def __new__(cls, *qrgs, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *qrgs, **kwargs)
        
        return cls.__instance
    

class MyClass(SingelTon):
    pass







A = MyClass()
B = MyClass()

print(A)        # <__main__.MyClass object at 0x00000180F205F090>
print(B)        # <__main__.MyClass object at 0x00000180F205F090>
print(A is B)   # True