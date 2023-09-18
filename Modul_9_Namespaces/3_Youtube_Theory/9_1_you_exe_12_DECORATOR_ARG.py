

def decor_with_args(arg):

    def simple_decorator(func):

        def simple_wrapper(*args, **kwargs):

            print(f'Before func {arg}')
            result = func(*args, **kwargs)
            print(f'After func {arg}')

            return result

        return simple_wrapper

    return simple_decorator


@decor_with_args('asd')
def mult(x, y):
    print('Mult')
    return x * y



print(mult(5, 6)) 

# Before func asd
# Mult
# After func asd
# 30