import shutil

# Робота з архівами

archive = shutil.make_archive('backup', 'zip', 'Temp/')
print(archive)

shutil.unpack_archive(archive, 'New_folder')