# В Інтернет-магазині зроблено 4 покупки: 
# на $34.34, $12.01, $17.42, $4.93. 
# Зі скількох доларів і центів складатиметься підсумкова сума.

price_1 = 34.34
price_2 = 12.01
price_3 = 17.42
price_4 = 4.93

sum = price_1 + price_2 + price_3 + price_4

dollars = int(sum // 1)
cents = int(sum % 1 * 100)

print(f'Sum {sum} or {dollars} dollars and {cents} cents')