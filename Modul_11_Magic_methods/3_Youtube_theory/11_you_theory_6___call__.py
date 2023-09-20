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
    
    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise ValueError('Index could be either 0 and 1')
        self.position[key] = value

    def __call__(self, value):
        print(value)
        print('This object has been callse')

        

char_position = Position(10, 20)

char_position('sdfsdf')     # This object has been callse

# sdfsdf
# This object has been callse

