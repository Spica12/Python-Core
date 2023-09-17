

class Animal:

    go_over = 0

    def __init__(self, nickname, age):

        self.__nickname = nickname               # __nickname - щоб ніхто не бачив
        self.age = age

    def get_info(self):
        return f'Animal name is {self.__nickname} and It\'s {self.age}'
    
    def step_count(self):
        self.go_over += 1000


dog = Animal('Alpha', 5)
cat = Animal('Alex', 3)

dog.step_count()

print(dog.get_info())
print(cat.get_info())

print(dog.nickname)
print(cat.nickname)




