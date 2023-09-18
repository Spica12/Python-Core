
def decorator(func):

    def inner(arg_one, arg_two):
        print('Hello')

        func(arg_one, arg_two)

        print('Good bye!')

    return inner

@decorator
def full_name(name, surname):
    print(f'My name is {name} {surname}')

full_name('Vitalii', 'Savenko')


decorator(full_name('one', 'two'))