import csv

with open('12_theory_5_1_use_csv.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Bill', 10])
    csv_writer.writerow(['12', 'John'])

# Bill,10
# 
# 12,John
# 

with open('12_theory_5_2_use_csv.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Bill', 10])
    csv_writer.writerow(['12', 'John'])

# Bill,10
# 12,John

users = [{'name': 'Bill', 'age': 12},
         {'name': 'John', 'age': 24},
         {'name': 'Maerry', 'age': 36}
]

def write_csv(file_name: str, data: list) -> None:

    if not data:
        return None

    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, list(data[0]), delimiter='\t')
        csv_writer.writeheader()
        csv_writer.writerows(data)

    return None
    
    
if __name__ == '__main__':
    write_csv('12_theory_5_3_use_csv.csv', users)  
    
