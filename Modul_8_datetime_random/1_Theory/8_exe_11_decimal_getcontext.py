from decimal import Decimal, getcontext

value = Decimal('1') / Decimal('3')
print(value)

getcontext().prec = 5

value_second = Decimal('1') / Decimal('3')
print(value_second)

