from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

phone_operators_number = defaultdict(list)

for ph in phone_numbers:
    if ph.startswith('050') or ph.startswith('095'):
        phone_operators_number['Vodaphone'].append(ph)
    elif ph.startswith('067') or ph.startswith('096'):
        phone_operators_number['Kyivstar'].append(ph)
    elif ph.startswith('063') or ph.startswith('093'):
        phone_operators_number['Lifecell'].append(ph)
    else:
        phone_operators_number['WTF'].append(ph)


print(phone_operators_number)
print(phone_operators_number.get('Vodaphone'))
print(phone_operators_number.get('Kyivstar'))
print(phone_operators_number.get('Lifecell'))
print(phone_operators_number.get('WTF'))