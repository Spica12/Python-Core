


def func(n):
    
    i = 0
    while i < n:
        print('Entry point')
        yield i
        print('After yield')
        i += 1



# Variant 1

generator = func(3)
next(generator) # Entry point
next(generator) # After yield
next(generator) # After yield

try:
    next(generator) # After yield
except StopIteration:
    print('Generator can\'t give')



# Variant 2 ----------------- Use for

generator = func(5)
for element in generator:
    print(element)
