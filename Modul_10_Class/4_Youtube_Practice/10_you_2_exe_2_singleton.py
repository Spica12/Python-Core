
class Singleton:

    instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_.instance, class_):
            class_.instance = object.__new__(class_, *args, **kwargs)
        return class_.instance
            


class A(Singleton):
    pass

a = A()
print(isinstance(a, A))     # True

a_1 = A()

print(a)
print(a_1)

# <__main__.A object at 0x00000237FF89EF10>
# <__main__.A object at 0x00000237FF89EF10>