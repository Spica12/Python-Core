from decimal import Decimal, getcontext

test = Decimal('3.14159')

precision = Decimal('0.000001')
getcontext().prec = 7
is_operation = True

pi = Decimal('3')
first = 2
second = 3
third = 4

while abs(pi - test) > precision:

    if is_operation:
        pi = pi + Decimal('4') / Decimal(first * second * third)
    else:
        pi = pi - Decimal('4') / Decimal(first * second * third)

    first += 2
    second += 2
    third += 2
    is_operation = not is_operation

print(pi.quantize(Decimal('1.0000')))
print(pi)