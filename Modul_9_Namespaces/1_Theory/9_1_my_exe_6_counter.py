

def counter():

    count = 0

    def inner(value:int):

        nonlocal count

        count += value

        return count
    
    return inner


if __name__ == '__main__':

    count = counter()
    print(count(1))
    print(count(1))
    print(count(1))
    print(count(-3))
    print(count(4))

    