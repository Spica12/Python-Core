
class Car:
    store_name = 'Sales Cars'

    def __new__(cls, *args, **kwargs):
        print('New instance created')
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, name, year, price, *args, **kwargs):
        self.name = name
        self.year = year
        self.price = price
        self.commision = None

    def __ge__(self, other):
        return self.price >= other.price

    def __ls__(self, other):
        return self.price <= other.price
    
    def __gt__(self, other):
        return self.price > other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __eq__(self, other):
        return self.price == other.price

    def buy(self):
        while self.commision == None:
            try:
                self.commision = float(input('Comission is not set!\n Comission '))
            except ValueError:
                print('Comission is invalid. Give correct value')
        self.price = self.price + self.price * self.commision
        return self.price
    
car_one = Car('Opel', 1998, 20000)
car_two = Car('Ford', 2015, 20000)

car_one.buy()
car_two.buy()

print(car_one == car_two)
print(car_one > car_two)