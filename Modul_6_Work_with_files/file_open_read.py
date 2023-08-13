print('--------------------------------------- read()')

file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

print(file.read())
# Hello world!        
# I love python       
# How are you?        
# I am fine, thank you
# My name is Vitalii

file.close

print('--------------------------------------- read(3)')

file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

print(file.read(3))
# Hel

file.close
print('---------------------------------------while, read(3)')

file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'r')

while True:

    file_data = file.read(3)
    print(file_data)

    if not file_data:
        break
# Hel
# lo
# wor
# ld!

# I
# lov
# e p
# yth
# on

# How
#  ar
# e y
# ou?

# I
# am
# fin
# e,
# tha
# nk
# you

# My
#  na
# me
# is
# Vit
# ali
# i
file.close

print('---------------------------------------, read(3)')
