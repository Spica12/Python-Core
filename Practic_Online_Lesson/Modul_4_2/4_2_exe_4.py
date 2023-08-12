from pathlib import Path
import sys

folder_path = Path(sys.argv[1])


def parse_folder(path):

    for element in path.iterdir():

        if element.is_dir():
            print(f'parse folder: This is folder - {element.name}')
        else:
            print(f'parse folder: This is file - {element.name}')


def parse_folder_recursion(path):

    for element in path.iterdir():
        if element.is_dir():
            parse_folder_recursion(element)
        else:
            print(f'parse folder: This is file - {element.name}')


if __name__ == '__main__':
    parse_folder(folder_path)
    parse_folder_recursion(folder_path)

# For start need due to CMD and add argument, for example '.'