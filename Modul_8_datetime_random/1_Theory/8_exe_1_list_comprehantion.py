squares = list()
for i in range(10):
    squares.append(i**2)
print(squares)


square_comp = [i**2 for i in range(10)]
print(square_comp)

print(squares == square_comp)
print('---------------------------')
