

def factorial(n, cache={}):
    if n < 0:
        raise ValueError
    
    def counter(n):
        result = 1
        for value in range(1, n+1):
            if value in cache:
                result = cache[value]
            else:
                result = value * cache.get(value-1, 1)
                cache[value] = result
                print('{} not in cache {}'.format(value, result))
        return result

    return counter(n)

print(factorial(4))
print(factorial(7))
print(factorial(4))
print(factorial(5))