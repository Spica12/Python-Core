# Декоратори

def complicated(x, y):
    return x / y


def logged_func(func):

    def inner(x, y):
        print(f'Called with {x = } and {y = }')
        result = func(x, y)
        print(f'{result = }')

        return result
    
    return inner



complicated = logged_func(complicated)
complicated(2, 3)