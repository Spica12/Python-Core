
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


char_1 = Character()
char_2 = Character()


print(char_1.hp)        # 100

char_1.name = 'Edelweiss'

print(char_1.name)      # Edelweiss
print(char_2.name)      # None


print('---------------------------------')
char_2.name = 'Bob'

print(char_1.name)      # Edelweiss
print(char_2.name)      # Bob


print('---------------------------------')
Character.hp = 300
print(char_1.hp)        # 300
print(char_2.hp)        # 300


print('---------------------------------')
Character.name = 'asd'
print(char_1.name)      # Edelweiss
print(char_2.name)      # None

char_3 = Character()
print(char_3.name)      # asd

