class Position:

    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    # Оператор == (equal)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Оператор != (not equal)
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y
        # Або
        return not self.__eq__(other)
    
    # Оператор < 
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    # Оператор > 
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    # Оператор <= 
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    # Оператор >= 
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    # Оператор and перевизначає  - &
    def __and__(self, other):
        pass

    # Оператор or перевизначає  - |
    def __or__(self, other):
        pass

    # Оператор xor перевизначає  - ^
    def __xor__(self, other):
        pass



char_position = Position(1, 1)
enemy_position = Position(1, 1)
portal_position = Position(2, 3)

print(char_position == enemy_position)  # True
print(char_position == portal_position) # False

print(char_position != enemy_position)  # False
print(char_position != portal_position) # True