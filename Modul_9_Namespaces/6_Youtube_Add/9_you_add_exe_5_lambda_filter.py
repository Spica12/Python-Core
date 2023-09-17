

def check_num(data):

    result = list()

    for n in data:
        ost = n % 2
        if ost:
            result.append(n)

    return result

if __name__ == '__main__':

    data = [1, 2, 3, 4, 5, 6]

    check_data = check_num(data)
    print(check_data)

    check_data_filter = filter(lambda n: n % 2,data)
    print(*check_data_filter)
