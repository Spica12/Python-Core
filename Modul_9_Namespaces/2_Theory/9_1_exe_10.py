
def say_hi(func, *args):

    def inner(*args):
        print('Hello')

        func(*args)

        print('Good bye!')

    return inner

@say_hi
def my_age(age):
    print(f'My name is {age}.')

my_age(5)


