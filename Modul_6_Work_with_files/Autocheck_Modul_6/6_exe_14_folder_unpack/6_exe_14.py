"""
Створіть функціонал для розпакування архіву.

Зробіть import пакету shutil

Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.

Функція нічого не повертає.
-----------------------------------
import shutil


def unpack(archive_path, path_to_unpack):
"""
import shutil


def unpack(archive_path, path_to_unpack):

    shutil.unpack_archive(archive_path, path_to_unpack)


archieve_path = 'Modul_6_Work_with_files/Autocheck_Modul_6/backup_folder.zip'
path_to_unpack = 'Modul_6_Work_with_files/Autocheck_Modul_6/6_exe_14_folder_unpack'

unpack(archieve_path, path_to_unpack)