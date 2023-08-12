from pathlib import Path

my_path = Path("C:\\willb\\")

print(my_path) # C:\willb

print(my_path.parent) # C:\

print(my_path.name) # willb





my_path = Path("C:\\Users\\user\\Downloads\\")

print(my_path.suffix) # .docx

print(my_path.exists()) # True

print(my_path.is_dir()) # False
print(my_path.is_file()) # True

for i in my_path.iterdir():
    print(i)

