

def pow_(base):

    def inner(value):
        return value ** base
    
    return inner


if __name__ == '__main__':

    pow__ = pow_(2)
    pow__2 = pow_(3)

    print(pow__(5))
    print(pow__(6))
    print(pow__(7))
    print(pow__(8))

    print(pow__2(5))
    print(pow__2(6))
    print(pow__2(7))
    print(pow__2(8))

