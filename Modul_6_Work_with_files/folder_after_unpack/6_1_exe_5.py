from pathlib import Path

file_name = Path('.')

try:
    with open(file_name / 'test_file.txt', 'r', encoding='utf-8') as file:
        print(file.readlines())
        file.seek(0)
        for line in file:
            print(line, end='')

except OSError:
    print('OSError')