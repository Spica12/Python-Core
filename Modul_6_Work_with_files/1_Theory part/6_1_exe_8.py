from pathlib import Path

new_dir = Path('.tmp')

if not new_dir.exists(): #  exists - перевірка чи існує файл або папка
    new_dir.mkdir() # mkdir - створити папку

# Або таким чином
new_dir.mkdir(exist_ok=True)