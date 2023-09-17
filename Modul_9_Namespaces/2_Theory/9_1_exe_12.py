

def outer(some_name):

    def decorator(func):

        def inner(*args, **kwargs):
            print(some_name)

            return func(*args, **kwargs)
        
        return inner
    
    return decorator


@outer('Check controls')
def adder(a, b):
    return a + b


print(adder(2, 5))