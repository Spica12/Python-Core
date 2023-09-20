
class Character:

    def __init__(self, name):

        self.name = name    # public
        self._damage = 10   # protected
        self.__hp = 100     # private

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, value):
        if value > 0 and value <= 100:
            self.__hp = value

    




char = Character('Biba')

print(char.hp)  # 100

char.hp = 80
print(char.hp)  # 80

char.hp = 1000
print(char.hp)  # 80

