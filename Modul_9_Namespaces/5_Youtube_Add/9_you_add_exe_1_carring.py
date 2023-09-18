
def hello_male(name):
    print(f'Mr. {name}')


def hello_female(name):
    print(f'Mrs. {name}')


def hello_pan(name):
    print(f'Пан. {name}')


MODES = {
    'm': hello_male,
    'f': hello_female,
    'pan': hello_pan
}


def greeting(mode):
    return MODES[mode]


def main():
    
    mr = greeting('m')
    mrs = greeting('f')
    pan = greeting('pan')

    mr('Vlad')      # Mr. Vlad
    mrs('Olga')     # Mrs. Olga
    pan('Vasyl')    # Пан. Vasyl


if __name__ == '__main__':
    main()