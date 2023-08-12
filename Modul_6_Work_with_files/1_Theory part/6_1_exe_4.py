from pathlib import Path

file_name = Path('.')

try:
    file = open(file_name / 'test_file.txt', 'r', encoding='utf-8')

    try:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end='')
    except OSError:
        print('OSError 2')
    finally:
        file.close()

except OSError:
    print('OSError')