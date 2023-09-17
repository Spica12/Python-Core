

def cache(func):

    data = {}

    def wrapper(*args):

        if args in data:
            return data[args]
        else:
            result = func(*args)
            data[args] = result
            return result
    
   

    return wrapper


@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(10))

print(fibonacci(10))
print(fibonacci(2))
print(fibonacci(5))
