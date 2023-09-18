def simple_decorator(func):

    def simple_wrapper():

        func()

    return simple_wrapper


def func():
    print('Hello world')

decor = simple_decorator(func)
decor()  # Hello world