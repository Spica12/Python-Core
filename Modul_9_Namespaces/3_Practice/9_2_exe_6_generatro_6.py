
def limited_generator(limit, magic_value):

    value = 0

    while value < limit:

        if value == magic_value:
            return
        
        yield value
        value += 1

check = limited_generator(10, 5)
print(2 in check)

check = limited_generator(10, 5)
print(7 in check)