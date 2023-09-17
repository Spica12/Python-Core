import sys


def logger(func):
    
    call_number = [0]

    def inner(*args, **kwargs):

        call_number[0] += 1
        sys.stdout.write(f'call [{call_number[0]}]: [{func.__name__}][{args}]\n')
        result = func(*args, **kwargs)
        sys.stdout.write(f'res: [{func.__name__}][{result}]\n')

        return result

    return inner

@logger
def multyplier(a, b):
    return a + b

multyplier(4, 7)

# call [1]: [multyplier][(4, 7)]
# res: [multyplier][11]

multyplier(9, 7)

# call [2]: [multyplier][(9, 7)]
# res: [multyplier][16]