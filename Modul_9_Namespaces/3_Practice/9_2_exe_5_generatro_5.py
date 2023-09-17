
def limited_generator(limit):

    value = 0

    while value < limit:
        yield value
        value += 1


for i in limited_generator(5):
    print(i)

    # 0
    # 1
    # 2
    # 3
    # 4


