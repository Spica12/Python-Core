# Open file
# fh = open('test_file.txt')
#  fh - файловий дескриптор (можна, наприклад file)

# After, you have to close file
fh = open('test_file.txt')
fh.close()

"""
--------------------------------------------------------------------------------------
| Mode | Meaning                                                                     |
--------------------------------------------------------------------------------------
|  'r' | Open only reading (default)                                                 |
|  'w' | Open on writing, вміст файлу видаляється, якщо не існує - створюється новий |
|  'x' | Open on writing if the file doesn't exist, else - excepting                 |
|  'a' | Open on дозапис, info addint in the end file                                |
|  'b' | Open in binary mode                                                         |
|  't' | Open in text mode (default)                                                 |
|  '+' | Open on reading and writing                                                 |
--------------------------------------------------------------------------------------
"""
# print('-------------------------------- read')
# # file.read(<symbols>) - read only next symbols 
# # file.read() - read all text from file
# fh = open('test_file.txt', 'w')
# symbols_written = fh.read()
# print(symbols_written)
# fh.close()


# print('-------------------------------- write')            

# fh = open('test_file.txt', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written)
# fh.close()

print('-------------------------------- seek, read') #                
fh = open('test_file.txt', 'w+')
fh.write('hello!')
fh.seek(0) # Перемістити каретку на 0 положення

first_two_symbols = fh.read(2) #Зчитати 2 символи
print(first_two_symbols) # he
fh.close()

fh = open('test_file.txt')
first_two_symbols = fh.read() # без аргументу, щоб зчитати весь файл
print(first_two_symbols) # hello!
fh.close()
print('--------------------------------')

fh = open('test_file.py', 'w')
fh.write('Hello!')
fh.seek(0)
fh.close()

fh = open('test_file.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break 
    print(symbol)  
fh.close()
# h
# e
# l
# l
# o
# !

print('-------------------------------- readline ')            
fh = open('test_file.txt', 'w')
fh.write('first line\nSecond line\nThird line')
fh.close()

fh = open('test_file.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()

# first line

# Second line

# Third line

print('-------------------------------- readlines ')             
fh = open('test_file.txt', 'w')
fh.write('first line\nSecond line\nThird line')
fh.close()

fh = open('test_file.txt', 'r')
while True:
    line = fh.readlines()
    if not line:
        break
    print(line) # ['first line\n', 'Second line\n', 'Third line']
fh.close()

print('-------------------------------- readlines ')             
file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

for line in file:
    print(line)


print('-------------------------------- seek ')
fh = open('test_file.txt', 'w')
fh.write('Hello')
fh.close()

fh = open('test_file.txt', 'r')
fh.seek(1)

second = fh.read(1)
print(second) # e
fh.close()

print('-------------------------------- tell ')
fh = open('test_file.txt', 'w+')
fh.write('Hello!') 

position = fh.tell()
print(position) # 6

fh.seek(1)
position = fh.tell()
print(position) # 1

fh.read(2)
position = fh.tell()
print(position) # 3
fh.close()

print('-------------------------------- try...except ')
fh = open('test_file.txt')

try: 
    # some_useful_function(fh)
except NameError:
    pass
finally:
    fh.close()

print('-------------------------------- with ')
with open('text.txt', 'w+') as fh:
    # some_useful_function(fh)

