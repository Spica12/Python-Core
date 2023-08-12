import scan
import normalize
from pathlib import Path
import shutil


def handle_file(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))


def handle_archive(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace('zip', ''))

    archive_folder = root_folder/new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))

    except shutil.ReadError:
        archive_folder.rmdir()
        return
    path.unli


def remove_empty_folders(path):
    if not any(path.iterdir()):
        path.rmdir()
        remove_empty_folders(path.parent)


def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)


def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        handle_file(file, folder_path, 'JPEG')

    for file in scan.jpg_files:
        handle_file(file, folder_path, 'JPG')

    for file in scan.png_files:
        handle_file(file, folder_path, 'PNG')

    for file in scan.txt_files:
        handle_file(file, folder_path, 'TXT')

    for file in scan.docx_files:
        handle_file(file, folder_path, 'DOCX')

    for file in scan.others:
        handle_file(file, folder_path, 'OTHERS')

    for file in scan.archives:
        handle_archive(file, folder_path, 'ARCHIVE')

    get_folder_objects(folder_path)


if __name__ == '__main__':
    path = sys.argv[1]
    print(f'Start in {path}')

    arg = Path(path)
    main(arg.resolve())