import functools

def simple_decorator(func):

    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):

        print('Before func')
        result = func(*args, **kwargs)
        print('After func')

        return result

    return simple_wrapper


@simple_decorator
def mult(x, y):
    return x * y



print(mult(5, 6))   # 30