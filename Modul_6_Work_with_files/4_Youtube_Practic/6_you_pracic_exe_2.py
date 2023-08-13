import os
from pathlib import Path

root_parent = 'Modul_6_Work_with_files/4_Youtube_Practic'
print(os.getcwd())


def walk(path, prev_dir_list):
    print(os.getcwd())

    os.chdir(path)

    list_dir = list(filter(os.path.isdir, os.listdir()))

    for el in list_dir:
        walk(fr'{path}/{el}', list_dir.remove(el))

    

walk('D:/GoIT/Python Core/Modul_6_Work_with_files/4_Youtube_Practic', [])