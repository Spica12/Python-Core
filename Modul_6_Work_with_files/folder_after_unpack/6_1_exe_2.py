import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print('Not enough parameters')
    quit() # Призупиняэ роботу файлу не викликаючі помилок

# Відкривати файл через try...except
try:
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        lines = list()
        for line in file:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        
        for line in lines:
            print(line)

except OSError:
    print('Error with right for file')