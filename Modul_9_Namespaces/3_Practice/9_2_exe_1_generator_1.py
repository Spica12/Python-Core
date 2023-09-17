squres_comp = [i**2 for i in range(10)]
print(squres_comp)      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squres_comp = (i**2 for i in range(10))
print(squres_comp)      # <generator object <genexpr> at 0x0000020C83CA9220>

for i in squres_comp:
    print(i)

    # 0
    # 1
    # 4
    # 9
    # 16
    # 25
    # 36
    # 49
    # 64
    # 81