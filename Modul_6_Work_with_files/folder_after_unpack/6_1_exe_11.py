from pathlib import Path

data = ['First line', 'Second line', 'Final line']

folder = Path('tmp')

with open(folder/'data.txt', 'w', encoding='utf-8') as file:
    for line in data:
        file.write(f'{line}\n')


with open(folder/'data.txt', 'w', encoding='utf-8') as file:
    file.writelines('First line\n', 'Second line\n', 'Final line\n')
    