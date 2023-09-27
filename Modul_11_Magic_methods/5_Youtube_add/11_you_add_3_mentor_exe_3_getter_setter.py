class Bus:

    def __init__(self, route: str) -> None:
        self.__route = None
        self.route = route

    @property
    def route(self) -> str:
        return f'{self.__route}'
    
    @route.setter
    def route(self, route: str) -> None:
        if len(route) > 3:
            raise ValueError('Route must be 3 characters')
        self.__route = route


    def __str__(self) -> str:
        return f'Bus on route {self.route}'
    

bus = Bus('385')
print(bus)      # <__main__.Bus object at 0x0000021931ABE690>
print(bus)      # Bus on route 385    (після додавання __str__)

bus.route = '657'
print(bus)      # Bus on route 657    (після додавання __str__)

print(bus.route)    # 657

try:
    bus1 = Bus('3852')
except ValueError as e:
    print(e)
