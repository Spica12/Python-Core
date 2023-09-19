
class SingelTon(object):
    __instance = None

    def __new__(cls, *qrgs, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *qrgs, **kwargs)
        
        return cls.__instance
    

class MyClass(SingelTon):
    pass