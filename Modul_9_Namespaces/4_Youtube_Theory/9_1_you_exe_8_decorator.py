def simple_decorator(func):

    def simple_wrapper(*args, **kwargs):

        print('Before func')
        func(*args, **kwargs)
        print('After func')

    return simple_wrapper


@simple_decorator
def func(text):
    print(text)


@simple_decorator
def mult(x, y):
    print(x * y)


func('asd')  # asd
mult(5, 6)   # 30