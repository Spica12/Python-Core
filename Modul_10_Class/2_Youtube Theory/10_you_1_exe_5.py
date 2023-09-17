class Character:

    count = 0

    hp = 100
    mp = 100

    def __init__(self, name, x, y):

        print('Init')

        Character.count += 1

        self.name = name
        self.x = x
        self.y = y

    def move(self):
        print(self)
        print('I am moving')

    def identify(self):
        print(self.name)

    def die(self):
        self.dead = True


first_char = Character(name='Bob', x=3, y=5)
second_char = Character(name='Alex', x=1, y=1)

print(first_char.name)            # Bob
print(first_char.x)               # 3
print(first_char.y)               # 5

print(second_char.name)            # Alex
print(second_char.x)               # 1
print(second_char.y)               # 4

