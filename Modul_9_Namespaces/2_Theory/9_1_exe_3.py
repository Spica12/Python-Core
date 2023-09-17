
def sum(a, b):
    return a + b

def minus(a, b):
    return a - b


def operation(a, b, func):
    return func(a, b)


def get_result(operation):
    if operation == '+':
        return sum
    elif operation == '-':
        return minus
    else:
        print('Unknown operation')

    

sum_func = get_result('+')
print(sum_func(6, 7))

sum_func = get_result('-')
print(sum_func(6, 7))