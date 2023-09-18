from time import time, sleep

def time_counter(func):

    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        time_passed = time() - start

        return result, time_passed
    
    return inner


@time_counter
def slepper(seconds):
    sleep(seconds)

    return seconds


print(slepper(10))
print(slepper(5))