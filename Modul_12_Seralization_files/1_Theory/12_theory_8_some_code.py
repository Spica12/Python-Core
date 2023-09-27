from copy import copy

class Car:

    def __init__(self, brand: str, seats: int) -> None:
        self.brand = brand
        self.seats = seats
        self.free_seats = [0] * self.seats

    def __copy__(self) -> object:
        new_car = Car(self.brand, self.seats)

        return new_car

print('-----------------------------------------------------------------')

car1 = Car('Honda', 16)

print(car1.free_seats)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('-----------------------------------------------------------------')

car2 = car1

car2.free_seats[0] = 1

print(car1.free_seats)  # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('-----------------------------------------------------------------')

car2 = copy(car1)

car2.free_seats[0] = 1

print(car1.free_seats)  # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

