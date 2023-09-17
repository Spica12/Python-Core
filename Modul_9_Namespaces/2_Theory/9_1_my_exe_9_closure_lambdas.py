def pow_(base):
    return lambda value: value ** base


if __name__ == '__main__':

    pow__ = pow_(2)
    print(pow__(5))


