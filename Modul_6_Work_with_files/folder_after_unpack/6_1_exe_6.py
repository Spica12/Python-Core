from pathlib import Path

list_dir = Path('.')

for element in list_dir.glob('*.py'): # glob() - це пошук за патерном
# * - все що до зірочки не важливо.
# .py - це те що нас цікавить
    print(element)