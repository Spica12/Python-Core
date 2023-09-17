

for i in filter(lambda x: x % 2, range(1, 10+1)):
    print(i)

# 1
# 3
# 5
# 7
# 9


some_string = 'aaANbvfNKsss dffPIUY'
for i in filter(lambda x: x.islower(), some_string):
    print(i)

    # a
    # a
    # b
    # v
    # f
    # s
    # s
    # s
    # d
    # f
    # f