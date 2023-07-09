# Дано радіус кола r (вводяться користувачем). Скласти програму 
# знаходження довжини кола та площі кола
# 
# Довжина кола - 2*Pi*R
# Площа кола - (Pi*R^2)/2

radius = float(input('Enter the radius:'))

PI = 3.14

length = round(2 * PI * radius, 2)
area = (PI * radius ** 2) / 2

print(f'Radius= {radius};\
        Length= {length};\
        Area= {area}')