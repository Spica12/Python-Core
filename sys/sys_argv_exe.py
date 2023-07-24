import sys
from sys_argv_exe_2 import main as greeting
from sys_argv_exe_2 import goodbye

def main():

    try:

        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'goodbye':
            goodbye()
        else:
            print(sys.argv)
    except IndexError:
        print('arguments must be "greet" or "goodbye"')


if __name__ == '__main__':
    main()