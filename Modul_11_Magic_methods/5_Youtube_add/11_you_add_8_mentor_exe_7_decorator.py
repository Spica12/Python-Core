def error_catch(func):

    def inner(a, b):

        try:
            return func(a, b)
        except ZeroDivisionError:
            return 0
    
    return inner


@error_catch
def div(a: int, b: int) -> float:
    return a / b

@error_catch
def mult(a: int, b: int) -> int:
    return a * b

def operations(a: int, b: int, func: callable) -> int|float:
    return func(a, b)


print(operations(1, 0, div))
print(operations(1, 5, div))