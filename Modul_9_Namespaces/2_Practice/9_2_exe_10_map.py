def nnumber_sqr(value):
    return pow(value, 2)


square_numbers = list(map(nnumber_sqr, [i for i in range(10)]))
print(square_numbers)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]