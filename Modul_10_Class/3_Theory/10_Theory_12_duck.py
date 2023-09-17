class Animal:

    def sound(self) -> None:
        pass


class Cat(Animal):

    def sound(self):
        return 'Meow'
    

class Dog(Animal):

    def sound(self):
        return 'Bark'
    


def pet_say(pet):
    print(pet.sound())


animal = Animal()
cat = Cat()
dog = Dog()


pet_say(cat)
pet_say(dog)
pet_say(animal)

