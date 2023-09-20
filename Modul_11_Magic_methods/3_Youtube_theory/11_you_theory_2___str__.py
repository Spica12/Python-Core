class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return 1        # Так робити не можна
        return f'({self.x}, {self.y})'


char_position = Position(10, 20)

print(char_position.x)  # 10
print(char_position.y)  # 20

print(char_position)    # (10, 20)