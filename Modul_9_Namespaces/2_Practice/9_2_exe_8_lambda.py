def foo(value):
    return value + 2


def baz(value):
    return value ** 2


def compose(func_one, func_two):
    return lambda value: func_one(func_two(value))


foobaz = compose(foo, baz)
print(foo(3), baz(3), foobaz(3))    # 5 9 11