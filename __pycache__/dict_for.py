numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for key in numbers:
    print(key)
    # 1
    # 2
    # 3

for key in numbers.keys():
    print(key)
    # 1
    # 2
    # 3

for val in numbers.values():
    print(val)
    # one
    # two
    # three

for key, value in numbers.items():
    print(key, value)
    # 1 one
    # 2 two
    # 3 three

# НЕ МОЖНА: видаляти з словника, додавати до словника в циклі
# МОЖНА: Змінювати значення