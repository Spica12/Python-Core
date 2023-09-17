class Character:

    name = None
    x = None
    y = None
    hp = 100
    mp = 100

    def move(self):
        print(self)
        print('I am moving')

    def identify(self):
        print(self.name)

    def die(self):
        self.dead = True


char = Character()

try:
    print(char.dead)
except AttributeError:
    print('You are not die yet')

print('------------------')

char.die()

try:
    print(char.dead)
except AttributeError:
    print('You are not die yet')
