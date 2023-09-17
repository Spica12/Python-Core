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


char_1 = Character('char_1')
char_2 = Character('char_2')
sword = Weapon()

char_1.pick_weapon_up(sword)
print(char_1.left_hand.type)

left_hand, right_hand = char_1.die()

char_2.pick_weapon_up(left_hand)
print(char_2.left_hand.type)
