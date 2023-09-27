import pickle

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name




animals = [
    Animal('Woolf'),
    Animal('Bobr')
]

print(animals)          # [<__main__.Animal object at 0x000001A7A696EF10>, <__main__.Animal object at 0x000001A7A696EED0>]

with open('12_theory_2_pickle.bin', 'wb') as f:
    pickle.dump(animals, f)


with open('12_theory_2_pickle.bin', 'rb') as f:
    animal_pickle = pickle.load(f)

print(animal_pickle)    # [<__main__.Animal object at 0x000001CEF7991BD0>, <__main__.Animal object at 0x000001CEF7991CD0>]


# Bootle neck - вузьке місце

