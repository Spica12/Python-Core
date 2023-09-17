
"""
class   
instance == object
"""

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


char_1 = Character()

char_1.move()   

# I am moving
# <__main__.Character object at 0x000001CDC61EEE50>

char_1.identify()       # None
char_1.name = 'Alex'
char_1.identify()       # Alex
