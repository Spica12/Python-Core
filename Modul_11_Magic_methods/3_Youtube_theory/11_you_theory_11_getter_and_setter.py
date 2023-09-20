
class Character:

    def __init__(self, name):

        self.name = name    # public
        self._damage = 10   # protected
        self.__hp = 100     # private

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, hp):
        if hp > 0 and hp <= 100:
            self.__hp = hp




char = Character('Biba')

print(char.get_hp())    # 100

char.set_hp(90)
print(char.get_hp())    # 90
char.set_hp(1000)
print(char.get_hp())    # 90        # не змінився, бо умова не виконалась в set_hp
