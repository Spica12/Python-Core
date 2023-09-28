import csv

file_name = '12_Notes_13_csv_table'
extension = '.csv'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\0_Notes\\"
file_full_name = path + file_name + extension


with open (file_full_name, 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer =csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open(file_full_name, 'r', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['first_name'], row['last_name'])