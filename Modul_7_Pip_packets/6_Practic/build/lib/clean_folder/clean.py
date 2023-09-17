import os
import sys
import shutil
from re import sub
from pathlib import Path


UKR_LETTERS = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
UKR_TRANSLATION = ("a", "b", "v", "g", 'g',"d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                    "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")
TRANS = {}

for key, ukr_letter in zip(UKR_LETTERS, UKR_TRANSLATION):

    TRANS[ord(key)] = ukr_letter
    TRANS[ord(key.upper())] = ukr_letter.upper()


def normalize(name):

    new_name = sub(r'\W', '_', name)
    new_name = new_name.translate(TRANS)

    return new_name


def move_archives(archieve, root_folder, dist):
    
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)

    name = archieve.name.removesuffix(archieve.suffix)
    archieve_folder = target_folder/name
    # print(f'Move {archieve}')
    shutil.unpack_archive(archieve, target_folder/f'{normalize(name)}')
    archieve.unlink()


def move_file(file, root_folder, dist):
    
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    name = file.name.removesuffix(file.suffix)
    # print(f'Move to {dist} next file: {file}')
    file.replace(target_folder/f'{normalize(name)}{file.suffix}')

def remove_empty_folder(folder):

    if not any(folder.iterdir()):

        folder.rmdir()
        remove_empty_folder(folder.parent)
        print(f'Empty folder {folder} have been deleted!')


def get_folder_objects(path):

    for folder in path.iterdir():

        if folder.is_dir():
            remove_empty_folder(folder)





image_files = list()
video_files = list()
document_files = list()
music_files = list()
archieves = list()
folders = list()
extensions = set()
unknown = set()

registered_extensions = {
    'IMAGE': ('JPEG', 'PNG', 'JPG', 'SVG'),
    'VIDEO': ('AVI', 'MP4', 'MOV', 'MKV'),
    'DOCUMENTS': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'MUSIC': ('MP3', 'OGG', 'WAV', 'AMR'),
    'ARCHIEVES': ('ZIP', 'GZTAR', 'TAR', 'GZ')
}

registered_files = {
    'IMAGE': image_files,
    'VIDEO': video_files,
    'DOCUMENTS': document_files,
    'MUSIC': music_files,
    'ARCHIEVES': archieves
}


def display_result_scan():

    print('This folder have next files:\n')
    for type, reg_folder in registered_files.items():
        print(f'{type}:')
        for item in reg_folder:
            print(f"      - {item}")

    print(f'FOLDERS:')
    for folder in folders:
        print(f'      - {folder}')
    print(f'\n{extensions = }')
    print(f'\n{unknown = }')


def get_extension(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):

    for element in folder.iterdir():

        if element.is_dir():
            if element.name not in ('IMAGE', 'VIDEO', 'DOCUMENTS', 'MUSIC', 'OTHER', 'ARCHIEVES'):
                folders.append(element)
                scan(element)
        else:

            extension = get_extension(element)
            new_name = folder/element.name

            if not extension:
                continue

            else:
                is_reg = False

                for key in registered_extensions:
                    
                    if extension in registered_extensions[key]:
                        container = registered_files[key]
                        extensions.add(extension)
                        container.append(new_name)
                        is_reg = True

                if not is_reg:
                    unknown.add(extension)


def sort(path):

    print(f"\nSTART SORTING: {path}\n")

    scan(path)

    display_result_scan()

    for image in image_files:
        move_file(image, path, 'IMAGE')

    for video in video_files:
        move_file(video, path, 'VIDEO')
    
    for music in music_files:
        move_file(music, path, 'MUSIC')

    for document in document_files:
        move_file(document, path, 'DOCUMENTS')

    for archieve in archieves:
        move_archives(archieve, path, 'ARCHIEVES')

    get_folder_objects(path)
    
    print(f'\n----- FINISHED -----\n')


def main():
    # path = Path('Modul_6_Work_with_files\Homework_6\TEMP')
    path = Path(sys.argv[1])

    sort(path)


if __name__ == '__main__':
    main()