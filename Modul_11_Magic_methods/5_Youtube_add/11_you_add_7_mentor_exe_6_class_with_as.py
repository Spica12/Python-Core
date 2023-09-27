class Bus:

    def __init__(self, route: str) -> None:
        self.route = route
        self.move = False   # Ознака чи стоїть автобус

    def start(self) -> None:
        self.move = True

    def stop(self) -> None:
        self.move = False

    def taking_passangers(self, passangers: int) -> None:
        if self.move:
            raise ValueError
        print(f'Bus takes: {passangers}')

    def __enter__(self):
        if self.move:
            self.stop()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.start()



bus = Bus('102')
print(bus.move)

with bus as b:
    b.taking_passangers(10)

print(bus.move)

