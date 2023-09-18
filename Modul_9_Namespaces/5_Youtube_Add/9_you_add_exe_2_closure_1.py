
def outer(x):

    def inner(y):
        print(f'{x} + {y} = {x + y}')
    
    return inner


def main():
    adder_two = outer(2)
    adder_two(2)                # 2 + 2 = 4
    adder_two(8)                # 2 + 8 = 10

    adder_three = outer(3)
    adder_three(2)              # 3 + 2 = 5
    adder_three(8)              # 3 + 8 = 11


if __name__ == '__main__':
    main()
