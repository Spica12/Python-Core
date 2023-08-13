with open('Modul_6_Work_with_files/test_file_writing_only.txt', 'w') as file:
    file.write('Hello')

print('-------------------------------')
# with open('Modul_6_Work_with_files/test_file_writing_only.txt', 'w') as file:
#     print(file.closed)  # False
#     file.write('Hello')
#     print(file.closed)  # False

# print(file.closed)      # True

print('-------------------------------')
# with open('Modul_6_Work_with_files/test_file_writing_only.txt', 'w') as file:

#     file.write('Hello')
#     raise ValueError
