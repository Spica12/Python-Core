# Напишіть функцію parse_folder, вона приймає єдиний параметр 
# path, який є об'єктом Path. Функція повинна просканувати 
# директорію path та повернути кортеж із двох списків. 

# Перший — це список файлів усередині директорії, 
# другий — список директорій.

# Приклад виводу функції:

# (['.gitignore', 'readme.md'],
#  ['.git', '.idea', '.vscode', 'module-01', 'module-02', 
#   'module-03', 'module-04', 'module-05', 'module-06', 
#   'module-07','module-08', 'module-09', 'module-10', 
#   'module-11', 'module-12'])
#  --------------------------------------------------
# def parse_folder(path):
#     files = []
#     folders = []
    
        
            
        
            
#     return files, folders
#  --------------------------------------------------
from pathlib import Path

def parse_folder(path):

    files = []
    folders = []

    # p = Path(path)

    for i in path.iterdir():

        if i.is_file():
            files.append(i.name)
        else:
            folders.append(i.name)   
            
    return files, folders


p = Path('D:\GoIT\Python Core\Modul_4')
print(parse_folder(p))
# print(parse_folder())