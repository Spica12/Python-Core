

class Weapon:

    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        return self.damage
    

class Knife(Weapon):

    def __init__(self):
        self.damage = 5

    def throw(self):
        return self.damage - 2


class Sword(Weapon):

    def __init__(self):
        self.damage = 15


class Axe(Weapon):

    def __init__(self):
        self.damage = 20


knife = Knife()
sword = Sword()
axe = Axe()

print(knife.kick_ass())
print(sword.kick_ass())
print(knife.throw())
print(axe.throw())
