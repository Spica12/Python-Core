
def first_second_counter():

    value = 0

    while True:
        yield 1
        yield 2


my_generation = first_second_counter()

for _ in range(6):
    print(next(my_generation))

    # 1
    # 2
    # 1
    # 2
    # 1
    # 2