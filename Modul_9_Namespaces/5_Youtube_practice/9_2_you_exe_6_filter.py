
print(help(filter))

for i in range(10):
    if i % 2:
        print(i)

# 1
# 3
# 5
# 7
# 9

x = list(filter(lambda i: i % 2, range(10)))


# Якщо True, то добавляє 
# Якщо False, то ігнорує
print(x)    # [1, 3, 5, 7, 9]

# 30:35