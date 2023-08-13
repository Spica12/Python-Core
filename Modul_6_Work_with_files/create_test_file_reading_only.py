file = open('Modul_6_Work_with_files/test_file_reading_only.txt', 'w')

test_data = ['Hello world!',
             'I love python',
             'How are you?',
             'I am fine, thank you',
             'My name is Vitalii']

for element in test_data:
    file.write(f'{element}\n')

file.close()