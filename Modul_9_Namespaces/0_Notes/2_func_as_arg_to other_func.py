def sum_func(x, y):
    return x + y


def substraction_func(x, y):
    return x - y


def tricky_func(x, y, func):
    return func(x, y)


sum_result = tricky_func(2, 3, sum_func)
min_result = tricky_func(2, 3, substraction_func)

print(sum_result)   # 5
print(min_result)   # -1


