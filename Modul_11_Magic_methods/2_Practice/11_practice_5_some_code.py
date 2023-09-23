from uuid import uuid1

# Для ідентифікації об'єктів в пітоні

"""
item
order
customer
``seller`
manufacturer
order -- містить список items
``seller` -- може додати/видалити товар у замовлення і підтвердити замовлення (відправити виробнику)
customer -- може переглядати товари по порядку
manufacturer -- може додати замовлення у внутрішній список замовлень, показати 
стан готовності (True/False) для замовлення і встановити замовлення як завершене
"""
class NotEnoughRights(Exception):

    def __init__(self, *value):
        self.value = value

    def __str__(self):
        return 'You have not enough rights for this.' + repr(self.args)


class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self, id_=None):
        if id_ is None:
            id = uuid1().int
        self.id = id
        self.items = list()
        self.total = 0

    def __add__(self, item):
        self.items.append(item)
        self.total += item.price

    def __sub__(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price


    def __str__(self):
        msg = f'Items\n'
        if self.items:
            for item in self.items:
                msg += f'{item.name}: {item.price}\n'

        msg += f'Total: {self.total}'

        return msg




class Person:

    def add(self, *args):
        raise NotEnoughRights

    def sub(self, *args):
        raise NotEnoughRights

    def view(self, *args):
        raise NotEnoughRights

    def check(self, *args):
        raise NotEnoughRights

    def confirm(self, *args):
        raise NotEnoughRights

    def complete(self, *args):
        raise NotEnoughRights
    

class Customer(Person):

    def view(self, order):
        return str(order)
    

class Seller(Person):

    def add(self, item, order=None):
        if order is None:
            order = Order()
        order + item
        return order
    
    def sub(self, item, order):
        order - item

    def view(self, order):
        return str(order)
    
    def confirm(self, order, manufacturer):
        manufacturer.add(order)


class Manufacturer(Person):

    def __init__(self) -> None:
        self.orders = dict()

    @property
    def order_list(self):
        return list(self.orders.keys())
    
    def add(self, order):
        self.orders[order.id] = False

    def view(self, order):
        if order.id in self.orders:
            return self.orders[order.id]
        
    def check(self, order):
        return self.orders(order.id)
    
    def complete(self, order):
        if order.id in self.orders:
            self.orders[order.id] = True



ball = Item('Ball', 10)
cap = Item('Cap', 5)
bag = Item('Bag', 15)

seller = Seller()
customer = Customer()
manufacturer = Manufacturer()

new_order = seller.add(ball)
print(seller.view(new_order))
print(customer.view(new_order))

seller.add(cap, new_order)
print(customer.view(new_order))

seller.sub(cap, new_order)
print(customer.view(new_order))

seller.add(bag, new_order)
print(customer.view(new_order))

seller.confirm(new_order, manufacturer)
print(manufacturer.order_list(new_order))

