
class SingelTon(type):
    __instance = {}

    def __new__(cls, *qrgs, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance[cls] = super(SingelTon, cls).__call__(*qrgs, **kwargs)
        
        return cls.__instance[cls]
    
# Python 2
class MyClass:
    __metaclass__ = SingelTon

# Python 3
class MyClass(metaclass=SingelTon):
    pass