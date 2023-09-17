from time import time


def args_logger(func):

    def inner(*args):

        if DEBUG:
            print(f'I am args logger. Args: {args}')

        result = func(*args)

        return result

    return inner


def result_logger(func):

    def inner(*args):

        result = func(*args)

        if DEBUG:
            print(f'I am a result logger. Result: {result}')

        return result

    return inner
   

def timer(func):

    def inner(*args):

        start = time()
        result = func(*args)
        stop = time()

        if DEBUG:
            print(f'I am a timer. Run time: {stop - start}')

        return result
    
    return inner



@timer
@result_logger
@args_logger
def calc(x, y):
    result = x + y

    return result




DEBUG = True

if __name__ == '__main__':
    print(calc(2, 5))