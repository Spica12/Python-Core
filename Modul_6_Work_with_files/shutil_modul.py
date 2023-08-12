import shutil

# shutil - модуль для роботи з архівами
# shutil може працювати з zip, tar, gz

# Заархівувати поточну папку
archive_name = shutil.make_archive('backup_from_modul_6_shutil', 'zip')
print(archive_name)

# Заархівувати syie папку, треба вказати шлях до неї в якості третього аргумента
# shutil.make_archive('<де зробити архів', 'zip', '<Що заархівувати>')
archive_name = shutil.make_archive('Modul_6_Work with files/backup_with_path', 'zip', 'Modul_6_Work with files/1_Theory part/')
print(archive_name)


# Для розпакування архівів використовується 
shutil.unpack_archive(archive_name, 'Modul_6_Work with files/folder_after_unpack')