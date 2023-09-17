def multiply(x):

    def inner(y):

        def func(z):

            return x * y * z

        return func

    return inner
    
multiply_ten = multiply(10)
multiply_ten_four = multiply_ten(4)


print(multiply_ten_four(5))     # 200

