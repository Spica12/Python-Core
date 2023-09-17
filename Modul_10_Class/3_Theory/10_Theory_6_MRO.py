

class A:
    x = 'a'


class B(A):
    pass

class C(A):
    ...

class D(B, C):
    x = 'c'

print(B.x)
print(D.x)

print(D.__mro__)