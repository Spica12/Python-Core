import json


data = {
    'name': 'Bill',
    'age': 33,
    'is_active': True,
    'games': ['WoW', 'Age of Empires'],
    'date': ('10.02.2023', '20.05.2005'),
    1999: 'GoIT',
}

with open('12_theory_4_json.json', 'w') as f:
    json.dump(data, f)

# Числові ключі стануть рядками
# tuple стане списком
# set взагалі не можна


with open('12_theory_4_json.json', 'r') as f:
    new_data = json.load(f)


print(data == new_data)

for key in data:
    print((type(key)))
print('-----------------')
for key in new_data:
    print((type(key)))