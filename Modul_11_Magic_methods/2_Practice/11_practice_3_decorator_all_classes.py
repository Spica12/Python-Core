import datetime
from time import sleep


def time_this(original_function):
    print('decorating')

    def inner(*qrgs, **kwargs):
        print('Start timer')

        before = datetime.datetime.now()

        func = original_function(*qrgs, **kwargs)

        after = datetime.datetime.now()
        print(f'Elapsed time = {after - before}')

        return func
    
    return inner


def time_all_class_methods(cls):

    class NewCls(object):
        def __init__(self, *qrgs, **kwargs):
            self.oInstance = cls(*qrgs, **kwargs)

        def __getattribute__(self, item):
            """
            """
            try:
                itemattr = super(NewCls, self).__getattribute__(item)
            except AttributeError:
                pass
            else:
                return attr
                
            attr = self.oInstance.__getattribute__(item)

            if type(attr) == type(self.__init__):
                return time_this(attr)
            else:
                return attr
            
    return NewCls

@time_all_class_methods
class Foo(object):
    def foo_func(self):
        print('Entering foo_func')
        sleep(2)
        print('Exit')


test = Foo()

test.foo_func()