from random import randint

def cycle_random_gen(min_val, max_val):
    while True:
        yield randint(min_val, max_val)


result = list()
random_gen = cycle_random_gen(10, 15)
for _ in range(15):
    value = next(random_gen)
    assert 10 <= value and value <= 15
    result.append(value)

print(result)   # [13, 13, 14, 11, 11, 11, 15, 10, 13, 11, 15, 15, 13, 13, 13]