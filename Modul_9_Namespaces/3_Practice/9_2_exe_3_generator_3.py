
def eight_bit_counter():

    value = 0

    while True:
        yield value
        value += 1


my_generation = eight_bit_counter()

for _ in range(6):
    print(next(my_generation))

    # 0
    # 1
    # 2
    # 3
    # 4
    # 5