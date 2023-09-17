

def greeting(name, second_name, third_name):
    print(f'My name is {name}, {second_name}, {third_name}')



def bot(func):

    def inner(*args, **kwargs):
        print(f'inner: func - {func.__name__}, args - {args}')

        print('Hello')
        # result = func(*args, **kwargs)
        func(*args, **kwargs)

        print('Good bye!')

        # result = result
    
    return inner


bot_says = bot(greeting)
bot_says('Bot', 'Second bot','Third bot')