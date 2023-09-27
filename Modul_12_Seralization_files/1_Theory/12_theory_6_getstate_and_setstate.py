import pickle


class Car:

    def __init__(self, brand: str) -> None:
        self.brand = brand

    def __getstate__(self) -> object:
        print('In __getstate__')

        attributes = self.__dict__.copy()
        attributes['file'] = None

        return attributes
    

    def __getstate__(self, value) -> None:
        print('In __setstate__')
        self.__dict__ = value
        self.file = 'my_file_name.bin'
    

car1 = Car('BMW')

with open('12_theory_6_some_code.bin', 'wb') as fh:
    pickle.dump(car1, fh)


with open('12_theory_6_some_code.bin', 'rb') as fh:
    car2 = pickle.load(fh)

print(car2.file)