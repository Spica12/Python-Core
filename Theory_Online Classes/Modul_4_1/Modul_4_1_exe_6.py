from pathlib import Path

parent_folder_path = Path('.')
print(parent_folder_path)

def parse_folder(path):
    for elements in path.iterdir():
        if elements.is_dir():
            print(f'parse_folder: This is folder - {elements.name}')
        else:
            print(f'parse_file: This is file - {elements.name}')


parse_folder(parent_folder_path)