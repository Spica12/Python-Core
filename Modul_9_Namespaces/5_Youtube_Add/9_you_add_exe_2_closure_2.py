
def outer(x):

    def inner(y):
        print(f'{x} + {y} = {x + y}')
    
    return inner

def get_cache(cache=None):

    if cache is None:
        cache = dict()

    def inner(n):

        print(cache)

        if n not in cache:
            print(f'Hard work {n}')
            cache[n] = sum([i for i in range(1, n+1)])

            return cache[n]
        
        else:
            print(f'Easy work {n}')
            return cache[n]
    
    return inner


def main():

    data = {5: 15, 10: 55, 12: 78, 113: 6441}
    
    calc = get_cache(data)
    print(calc(5))
    print(calc(5))
    print(calc(10))
    print(calc(5))
    print(calc(12))
    print(calc(113))


if __name__ == '__main__':
    main()
