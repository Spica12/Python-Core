
def odd_squares(limit):

    for value in range(limit):

        if value % 2:
            yield pow(value, 2)


limit = 15
get_value = filter(lambda value: bool(value % 2), map(lambda x: pow(x, 2), list(range(limit))))

for result in zip(get_value, odd_squares(limit)):
    print(result[0], result[1])

# 1 1
# 9 9
# 25 25
# 49 49
# 81 81
# 121 121
# 169 169