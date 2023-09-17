from functools import reduce

values = [3, 4, 6, 12, 34, 9]

sum_numbers = reduce(lambda x, y: x + y, values)
print(sum_numbers)  # 68