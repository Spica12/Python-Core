file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

print(file.read(5)) # Hello

# Поставити на позицію, що треба
file.seek(10)
# 1234567890
# Hello world!
print(file.read(1)) # d

file.close()