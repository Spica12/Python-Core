from pathlib import Path

new_dir = Path('D:/GoIT/Python Core/Theory_Online Classes/Modul_6_1/tmp/tmp')

if not new_dir.exists(): #  exists - перевірка чи існує файл або папка
    new_dir.mkdir() # mkdir - створити папку

# Або таким чином
new_dir.mkdir(parents=True, exist_ok=True)

# Чи зберігається така система папок, 