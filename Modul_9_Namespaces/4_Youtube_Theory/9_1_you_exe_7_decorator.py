def simple_decorator(func):

    def simple_wrapper():

        print('Before func')
        func()
        print('After func')

    return simple_wrapper

@simple_decorator
def func():
    print('Hello world')

func()  # Hello world