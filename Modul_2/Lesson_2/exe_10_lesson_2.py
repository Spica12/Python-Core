# У банк поклали 100 доларів під 5 % річних. Скласти програму 
# обчислення кількості грошей на рахунку через 10 років. (складні 
# щомісячні відсотки)

PERCENT = 0.05

deposit = 100
waiting_year = 10

print(round(deposit * (1 + PERCENT / 12) ** (12 *10), 2))

for year in range(1, waiting_year + 1):
    new_deposite = deposit * (1 + PERCENT / 12) ** 12
    deposit = new_deposite

print(round(deposit, 2))
