# Скласти програму обчислення площі та гіпотенузи прямокутного 
# трикутника, якщо відомі його катети (вводяться користувачем)

katet_a = float(input('Enter first katet: '))
katet_b = float(input('Enter second katet: '))

gipotenuza_c = (katet_a ** 2 + katet_b ** 2) ** 0.5
area = (katet_a * katet_b) / 2

print(f'Giputenuza = {gipotenuza_c}; Area = {area}')