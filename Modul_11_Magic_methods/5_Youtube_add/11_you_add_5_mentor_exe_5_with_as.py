


with open('myfile.txt', 'w') as fh:
    fh.write('World Hello!')

# fh - змінна глобальна а не локальна, тому можна використати поза with
print(fh.closed)    # True
