class A:

    field = None

    def method(self):
        pass


print(A.__dict__)


# {'__module__': '__main__', 
#  'field': None, 
#  'method': <function A.method at 0x000001B8C0A49E40>, 
#  '__dict__': <attribute '__dict__' of 'A' objects>, 
#  '__weakref__': <attribute '__weakref__' of 'A' objects>, 
#  __doc__': None}


# Спец об'єкт що зберегіає всі атрибути класу