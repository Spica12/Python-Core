squares = set()
for i in range(10):
    squares.add(i**2)
print(squares)


squares_comp = {i**2 for i in range(10)}
print(squares_comp)

print(squares == squares_comp)
