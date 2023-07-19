

def foo():
    print('Hello!')


def spam():
    pass


foo()
spam()

# -----------------------------------

def foo() -> int:
    a: int = 4
    b: int = 8

    return a + b

result: int = foo()
print(result)

# -----------------------------------

def add(a: int, b: int) -> int:
    """
    Function of adding two numbers

    Input:
    a = integer
    b = integer

    Output:
    :return - integer
    """

    a: int = 4
    b: int = 8

    return a + b

result: int = add(2, 4)
print(result)

# -----------------------------------

def add(a, b):
    return a + b

print(add(2, 3))


def print_result(*args):
    for value in args:
        print(value)

print_result(2, 3, 4, 5, 6, 8)


def sum(*args):

    print(args)
    result = 0

    for value in args:
        try:
            result += value
        except ValueError:
            continue
    
    return result

print(sum(4, 5, 6, 7, 8, 9))

print('---------------------------------')

words = {1: 'Python', 'may': 45}

def result(**kwargs): # KeyWordsArguments
    print(kwargs)

result(hello='Python', may=45)

print('---------------------------------')

def multiply(a, b, c=None):
    if c is None:
        return a * b
    else:
        return a * b * c
    
print(multiply(2, 4, 5))
print(multiply(2, 4))

print('---------------------------------')

def gretting(**kwargs):
    name = kwargs.get('name', 'Unknown')
    age = kwargs.get('age', None)

    return f'Hello {name}, you are have {age} years old'

print(gretting())
print(gretting(name='Oleh', age=100))

print('---------------------------------')

x = 10

def foo():
    x = 5

    print(x)

foo()
print(x)

print('---------------------------------')

def security(password):

    def divide():
        nonlocal password

        return password / 2

    return divide()

print(security(3456))

print('----------------Fibonachi-----------------')

def fibonachi(n):
    # 0, 1, 1, 2, 3, 5, 8, 13 ...

    return n if n==1 or n==0 else fibonachi(n-2)+fibonachi(n-1)
    
print(fibonachi(8))

print('----------------Factorial-----------------')

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(5))

print('----------------Power-----------------')

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)
    
print(power(2, 3))
print(pow(2, 3))

print('----------------Power-----------------')

def result(*args):
    print(args)
    print(args[1:3])

result(76, 436, 'fsdfsd', 'sdfsdf', 3451)

print('----------------Polindrom-----------------')

def is_palindrome(word):
    print(word)
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])
    
print(is_palindrome('Python'))
print(is_palindrome('qwertytrewq'))

print('---------------------------------')

print('---------------------------------')

operation_dict = dict()

user_input = input('Enter sentence: ')

for char in user_input:

    if char not in operation_dict.keys():
        operation_dict[char] = 1
    else:
        operation_dict[char] += 1

print(operation_dict)
print(operation_dict.keys())
print(operation_dict.values())