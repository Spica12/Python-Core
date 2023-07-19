from py_1 import get_name


def goodbye(name):
    print(f'Goodbye {name}')


def main():
    name = get_name()
    goodbye(name)

if __name__ == '__main__':
    print(f'__name__ == {__name__}')
    main()