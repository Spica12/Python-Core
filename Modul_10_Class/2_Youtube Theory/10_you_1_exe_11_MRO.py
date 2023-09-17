
class A:

    def hello(self):
        print('hello A')


class B:

    def hello(self):
        print('hello B')


class C:

    def hello(self):
        print('hello C')


class D(A, B, C):
    pass



print(D.hello(D))

# 1:37