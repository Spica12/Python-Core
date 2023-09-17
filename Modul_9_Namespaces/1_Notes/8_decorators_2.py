

def logged_func(func):

    def inner(x, y):
        print(f'Called with {x = } and {y = }')
        result = func(x, y)
        print(f'{result = }')

        return result
    
    return inner


@logged_func
def complicated(x, y):
    return x / y


complicated(2, 5)