class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    def __str__(self):
        # return 1        # Так робити не можна
        return f'str: ({self.x}, {self.y})'

    def __repr__(self):
        return f'repr: ({self.x}, {self.y})'
    
    def __getitem__(self, key):
        return self.position[key]



char_position = Position(10, 20)

print(char_position.x)  # 10
print(char_position.y)  # 20

print(char_position)    # str: (10, 20)

print(repr(char_position))  # repr: (10, 20)

print(char_position[0]) # 10
print(char_position[1]) # 20


