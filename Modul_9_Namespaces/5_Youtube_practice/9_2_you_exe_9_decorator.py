def decorator(func):

    def inner(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return inner


@decorator
def func(x, y):
    return x + y

print(func(5, 3))       # 8