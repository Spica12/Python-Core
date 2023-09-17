
x = 10#int(input('X = '))
y = 5#int(input('Y = '))
operator = '+'#input('Operator: ')

if operator == '+':
    print(x + y)
elif operator == '-':
    print(x - y)
elif operator == '*':
    print(x * y)

# ----------- Next version: Functional--------------

def operate(x, y, operator):

    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y

    return result

print(operate(10, 5, '+'))

# ----------- Next version: --------------

def summ(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def pow(x, y):
    return x ** y


operations = {
    '-': sub,
    '+': summ,
    '*': mul,
    '**': pow
}

print(operations['+'](10, 5))


# ----------- The best version: --------------

def summ(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def pow(x, y):
    return x ** y


def operate(operator):
    return operations[operator]


operations = {
    '-': sub,
    '+': summ,
    '*': mul,
    '**': pow
}

handler_sum = operate('+')
print(handler_sum(10, 5))

print(operate('+')(10, 5))