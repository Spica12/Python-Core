class Animal:

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):

    def __init__(self, name: str) -> None:
        super().__init__(name)