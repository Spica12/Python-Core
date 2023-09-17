from decimal import Decimal, getcontext

a = 0.1
b = 0.2
print(a + b)        # 0.30000000000000004
print('------------------------------------------------ .getcontext()')

getcontext().prec = 5

print(Decimal('0.1'))
