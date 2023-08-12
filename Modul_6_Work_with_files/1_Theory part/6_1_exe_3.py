import sys

NUM_LINES = 10

if len(sys.argv) != 1:
    print('Set th file names as parameters in terminal')
    quit() # Призупиняэ роботу файлу не викликаючі помилок

print(sys.argv)
for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line)

    
    except OSError:
        print('Error with right for file {file_name}')