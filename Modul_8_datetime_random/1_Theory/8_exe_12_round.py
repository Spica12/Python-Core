from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

number = Decimal('1.45')
print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))
print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))

print(Decimal('3.145678934').quantize(Decimal('1.000')))


number_one = 1.37
number_two = 1.5

first = Decimal.from_float(number_one)
print(first)

second = Decimal.from_float(number_two)
print(second)

first = Decimal(str(number_one))
print(first)

second = Decimal(str(number_two))
print(second)