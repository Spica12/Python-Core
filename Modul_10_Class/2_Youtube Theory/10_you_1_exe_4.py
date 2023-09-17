class Character:

    count = 0

    hp = 100
    mp = 100

    def __init__(self):

        print('Init')

        Character.count += 1

        self.name = None
        self.x = None
        self.y = None

    def move(self):
        print(self)
        print('I am moving')

    def identify(self):
        print(self.name)

    def die(self):
        self.dead = True


char = Character()
print(char.name)            # None
print(char.x)               # None
print(char.y)               # None

char_2 = Character()
print(char.name)            # None
print(char.x)               # None
print(char.y)               # None

print(Character.count)      # 2