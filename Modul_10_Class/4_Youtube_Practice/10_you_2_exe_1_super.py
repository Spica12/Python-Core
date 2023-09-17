# print(help(super))

"""
class super(object)
 |  super() -> same as super(__class__, <first argument>)
 |  super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 |  Typical use to call a cooperative superclass method:
 |  class C(B):
 |      def meth(self, arg):
 |          super().meth(arg)
 |  This works for class methods too:
 |  class C(B):
 |      @classmethod
 |      def cmeth(cls, arg):
 |          super().cmeth(arg)
 |
 |  Methods defined here:
 |
 |  __get__(self, instance, owner=None, /)
 |      Return an attribute of instance, which is of type owner.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |      the type of the instance invoking super(); may be None
 |
 |  __thisclass__
 |      the class invoking super()
"""

class A:

    def __init__(self):
        print('Hello, I am A')


class B(A):

    def __init__(self):
        print('Hello, I am B')


a = A()
b = B()

# Hello, I am A
# Hello, I am B 



class A:

    def __init__(self):
        print('Hello, I am A')


class B(A):

    def __init__(self):
        super().__init__()                      # Використати конструктор з батьківського класу
        print('Hello, I am B')


a = A()
b = B()

# Hello, I am A

# Hello, I am A
# Hello, I am B