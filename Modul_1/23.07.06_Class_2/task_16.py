# Для кава-брейків на конференції закуплено: х круасанів, у стаканчиків, 
# z упаковок кави. 
# 
# Ціна круасана $1.04, 
# ціна стаканчика - $0.34, 
# ціна упаковки кави $4.42. 
# 
# Скласти програму, яка обчислює, скільки повних доларів пішло на 
# закупівлю їжі для кава-брейків, і яка її вартість у доларах і центах.

croissants = int(input('Enter croissants: '))
cups = int(input('Enter cups: '))
coffee = int(input('Enter coffee: '))

PRICE_CROISSANT = 1.04
PRICE_CUP = 0.34
PRICE_COFFEE = 4.42

sum = PRICE_CROISSANT * croissants + \
      PRICE_CUP * cups + \
      PRICE_COFFEE * coffee

dollars = int(sum)
cents = int(sum * 100)
print(f'{dollars} dollars or {cents} cents')