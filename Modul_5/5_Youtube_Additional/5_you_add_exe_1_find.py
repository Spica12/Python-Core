

files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']

for file in files:

    index = file.find('.')
    suffix = file[index+1:]

    if index != -1:
        print(f'File: {file} Index: {index} Suffix: {suffix}')
    else:
        print(f'File: {file} Suffix: not found')

print('-----------------------------------------------')

for file in files:

    try:

        index = file.index('.')
        suffix = file[index+1:]
        print(f'File: {file} Index: {index} Suffix: {suffix}')

    except ValueError:
        print(f'File: {file} Suffix: not found')

print('-----------------------------------------------')
print('-----------------------------------------------')


files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'backup.tar.gz']

for file in files:

    index = file.rfind('.')
    suffix = file[index+1:]

    if index != -1:
        print(f'File: {file} Index: {index} Suffix: {suffix}')
    else:
        print(f'File: {file} Suffix: not found')

