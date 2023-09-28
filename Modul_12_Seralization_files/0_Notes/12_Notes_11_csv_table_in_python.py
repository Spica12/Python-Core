import csv

file_name = '12_Notes_11_csv_table_in_python'
extension = '.csv'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"
file_full_name = path + file_name + extension


with open(file_full_name, 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


with open(file_full_name, 'r', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))
