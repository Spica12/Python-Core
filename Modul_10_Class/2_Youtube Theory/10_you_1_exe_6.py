# SOLID
# S - Single responsibility

class Character:

    count = 0

    hp = 100
    mp = 100

    def __init__(self, name, x=0, y=0):

        print('Init')

        Character.count += 1
        
        self.name = name
        self.x = x
        self.y = y

        self.left_hand = None
        self.right_hand = None

    def move(self):
        print(self)
        print('I am moving')

    def identify(self):
        print(self.name)

    def die(self):
        self.dead = True
        return self.left_hand, self.right_hand

    def pick_weapon_up(self, weapon):

        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print('I am full')

    def show_weapon(self):
        return self.left_hand, self.right_hand


class Weapon:

    def __init__(self):
        self.type = 'sword'
        self.damage = 10


char = Character('Bob')

# Opening a chest
sword_1 = Weapon()

char.pick_weapon_up(sword_1)

# 1:10:00

print(char.left_hand.type)
