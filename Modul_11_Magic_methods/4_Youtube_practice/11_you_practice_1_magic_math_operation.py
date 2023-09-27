

class Position:

    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    # Додавання
    def __add__(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    # Різниця
    def __sub__(self, other):
        pass

    # Множення
    def __mul__(self, other):
        pass

    # Ділення
    def __div__(self, other):
        pass

    # в ступінь 
    def __pow__(self, other):
        pass

    # Є інші ще...
    



char_position = Position(1, 1)
enemy_position = Position(3, 3)

print(char_position + enemy_position)
