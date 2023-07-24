def get_name():
    name = input('Write your name: ')

    return name


def goodbye(name):
    print(f'Goodbye {name}')


def greet(name):
    print(f'Hello {name}')


def main():

    name = get_name()
    greet(name)


if __name__ == '__main':
    main()