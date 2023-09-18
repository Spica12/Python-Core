# Currying Карування

# Каррування — це перетворення функції від багатьох аргументів у набір функцій, 
# кожна з яких є функцією від одного аргументу. Ми можемо передати частину 
# аргументів у функцію і отримати назад функцію, що очікує інші аргументи.


def handle_operation(x, y, operator):

    if operator == '-':
        return x - y
    elif operator == '+':
        return x + y
    

handle_operation(2, 3, '+')
handle_operation(2, 3, '-')


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handler(operator):
    return OPERATIONS[operator]


print(get_handler('+')(2, 3))
print(get_handler('-')(2, 3))