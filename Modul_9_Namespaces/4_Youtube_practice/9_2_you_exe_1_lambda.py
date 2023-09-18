def func(x, y, z):
    return x * y * z


# Щоб не створювати змінну, треба завернути lambda в дужки ()
# і після в других дужках передати аргументи
print((lambda x, y, z: x * y * z)(10, 10, 10))      # 1000

print((lambda x, y, z: x * y * z)(z=10, x=11, y=10))      # 1100

print(func(10, 10, 10))     # 1000 