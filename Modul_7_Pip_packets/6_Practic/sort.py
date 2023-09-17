import sys
import shutil
from pathlib import Path
from scan import *
from normalize import *


def main():
    # path = Path('Modul_6_Work_with_files\Homework_6\TEMP')
    path = Path(sys.argv[1])

    sort(path)


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


if __name__ == '__main__':
    main()