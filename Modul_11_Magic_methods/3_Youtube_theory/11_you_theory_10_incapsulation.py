# public
# protected
# private


class Character:

    def __init__(self, name):

        self.name = name    # public
        self._damage = 10   # protected
        self.__hp = 100     # private


class Enemy(Character):
    pass



# public
char = Character('Jack')
print(char.name)    # Jack
char.name = 'Biba'
print(char.name)    # Biba   



# protected - 
# Доступ є, але розробнику не варто використовувати поза об'єктом
print(char._damage)    # 10
char._damage = 20
print(char._damage)    # 20


# private
# print(char.__hp)    # AttributeError: 'Character' object has no attribute '__hp'

print(char.__dict__)    # {'name': 'Biba', '_damage': 20, '_Character__hp': 100}
print(char.__dict__['_Character__hp'])  # 100
char.__dict__['_Character__hp'] = 80
print(char.__dict__['_Character__hp'])  # 80
