
MASTER_WORK_PRICE = 75
HUNDRED_PAPER_PRICE = 120
INC_PRICE = 20

def profit(p, n):

    if n % 100 != 0:
        return 'Error, not multiple by 100'

    number_hundreds = n // 100

    return n * p - number_hundreds * (MASTER_WORK_PRICE + HUNDRED_PAPER_PRICE + INC_PRICE)

print(profit(2.5, 1000))
print(profit(5, 145))