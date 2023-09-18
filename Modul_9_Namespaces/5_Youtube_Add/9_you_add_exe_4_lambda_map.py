

def get_ost(data):

    result = list()

    for n in data:
        ost = n % 2
        result.append(ost)

    return result


if __name__ == '__main__':

    data = [1, 2, 3, 4, 5, 6]

    ost_1 = get_ost(data)

    print(ost_1)
    print(*ost_1)

    ost_2 = map(lambda n: n % 2, data)
    print(*ost_2)
