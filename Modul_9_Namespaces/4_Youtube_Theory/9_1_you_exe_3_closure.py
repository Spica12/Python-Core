def multiply(x):

    def inner(y):

        return x * y


    return inner
    
multiply_ten = multiply(10)
multiply_three = multiply(3)

print(multiply_ten(10), multiply_three(10))     # 100 30

