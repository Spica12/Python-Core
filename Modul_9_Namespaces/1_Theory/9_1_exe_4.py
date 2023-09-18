

def outer_func(name):

    message = 'Hello'

    def inner_func(message, name):
        greting = f'{message}, {name}'
        return greting
    
    return inner_func(message, name)


print(outer_func('Oleh'))