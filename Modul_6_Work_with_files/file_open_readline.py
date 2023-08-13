print('----------------------------- readline')

file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

print(file.readline())
print(file.readline())
print(file.readline())

# Hello world!
# 
# I love python
# 
# How are you?
# 

file.close()

print('----------------------------- ')

file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

for line in file:
    print(line)

# Hello world!
# 
# I love python
# 
# How are you?
# 
# I am fine, thank you
# 
# My name is Vitalii
# 


file.close()
