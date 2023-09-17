import random

print(random.randint(0, 20))
print(random.randrange(0, 100, 3))
print(random.choice(['balck', 'white', 'red']))
print(random.choices(['balck', 'white', 'red'], k=6, weights=[1, 2, 3]))


range_list = list(range(10))
print(range_list)

random.shuffle(range_list)
print(range_list)