files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']

for file in files:
    index = file.find('.')
    if index != -1:
        suffix = file[index+1:]
        print(f'File: {file} Index {index} Suffix: {suffix}')
    else:
        print(f'File: {file} Suffix: Not found')

print('-----------------------------------------')
for file in files:
    try:
        index = file.index('.')
        if index != -1:
            suffix = file[index+1:]
            print(f'File: {file} Index {index} Suffix: {suffix}')
    except ValueError:
        print(f'File: {file} Suffix: Not found')

files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'backup.tar.gz']

print('-----------------------------------------')

for file in files:
    index = file.rfind('.')
    if index != -1:
        suffix = file[index+1:]
        print(f'File: {file} Index {index} Suffix: {suffix}')
    else:
        print(f'File: {file} Suffix: Not found')
    