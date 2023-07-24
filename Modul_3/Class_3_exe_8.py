


MASTER_WORK_PRICE = 75
HUNDRED_PAPER_PRICE = 120
INC_PRICE = 20

TAX_MIN = 0.05
TAX_MID = 0.08
TAX_MAX = 0.15

def profit(p, n):

    if n % 100 != 0:
        return 'Error, not multiple by 100'

    number_hundreds = n // 100

    return n * p - number_hundreds * (MASTER_WORK_PRICE + HUNDRED_PAPER_PRICE + INC_PRICE)


def profit_after_tax(p, n):

    profit_before_tax = profit(p, n)

    if profit_before_tax < 100_000:
        return profit_before_tax * (1 - TAX_MIN)
    elif profit_before_tax < 1_000_000:
        return profit_before_tax * (1 - TAX_MID)
    else:
        return profit_before_tax * (1 - TAX_MAX)

print(f'Before tax {profit(2.5, 500000)}')
print(f'After tax {profit_after_tax(2.5, 500000)}')
