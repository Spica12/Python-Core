values = [100, -3, 10, 0, -100, 33]

positive_numbers = list(filter(lambda elem: elem > 0, values))
print(positive_numbers)    # [100, 10, 33]