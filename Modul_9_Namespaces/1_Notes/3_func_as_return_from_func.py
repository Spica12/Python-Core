
#  Можемо працювати з функціями у Python точно так, як 
# з будь-якими іншими типами даних: можемо повертати з функції інші функції.

def sum_func(x, y):
    return x + y


def substraction_func(x, y):
    return x - y


def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return substraction_func
    else:
        print('Unknown operator')


sum_action_function = get_operator('+')
print(sum_action_function(2, 3))    # 5

sum_action_function = get_operator('-')
print(sum_action_function(2, 3))    # -1


