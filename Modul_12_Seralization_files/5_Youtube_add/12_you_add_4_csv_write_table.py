from csv import DictWriter
import json


file_json = 'D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\5_Youtube_add\\12_you_add_3_users.json'
file_csv = 'D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\5_Youtube_add\\12_you_add_5_users.csv'


def get_users():
    with open(file_json, 'r') as fh:
        users = json.load(fh)
        
        return users

def write_table():
    users = get_users()

    with open(file_csv, 'w', encoding='utf-8', newline='') as fh:
        fields_name = users[0].keys()
        writer = DictWriter(fh, delimiter=';', fieldnames=fields_name)
        writer.writeheader()
        for row in users:
            writer.writerow(rowdict=row)
        print('CSV table was created')

if __name__ == '__main__':
    write_table()