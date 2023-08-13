import os

print(os.getcwd())      # D:\GoIT\Python Core

# Перейти в папку os
os.chdir('os')

print(os.getcwd())      # D:\GoIT\Python Core\os

# Повернутись в поперденю папку
os.chdir('..\\')

print(os.getcwd())      # D:\GoIT\Python Core