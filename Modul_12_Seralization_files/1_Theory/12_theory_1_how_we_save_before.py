class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


def save_to_file(file_name: str, objects: list[Animal]) -> None:

    data = '\n'.join([o.name for o in objects])

    with open(file_name, 'w') as f:
        f.write(data)


def load_from_file(file_name: str) -> list[Animal]:

    data = None

    try:
        with open(file_name) as f:
            data = f.read()
            if data:
                return [Animal(name) for name in data.split('\n')]
    except FileNotFoundError:
        return []
    if not data:
        return []
    
    


tiger = Animal('Tiger')

animals = load_from_file('12_theory_1_how_we_save_before.txt')
print(animals)

while True:
    animal = input('Type animal name or enter for end: ')
    if not animal:
        save_to_file('12_theory_1_how_we_save_before.txt', animals)
        break
    animals.append(Animal(animal))

print([a.name for a in animals])