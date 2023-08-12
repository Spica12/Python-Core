from pathlib import Path

try:
    tmp = Path('D:/GoIT\Python Core/Theory_Online Classes/Modul_6_1/test_file copy.txt')
    tmp.unlink() # Видалити файл
    

except FileNotFoundError:
    print('OSError')