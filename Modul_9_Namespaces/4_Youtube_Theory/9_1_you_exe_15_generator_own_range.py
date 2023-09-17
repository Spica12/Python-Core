

def my_range(x, y):

    while x < y:
        yield x
        x += 1


for i in my_range(0, 5):
    print(i)

# 0
# 1
# 2
# 3
# 4