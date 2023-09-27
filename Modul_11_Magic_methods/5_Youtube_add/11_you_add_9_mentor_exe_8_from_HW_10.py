class Phone:

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value
    
    def __eq__(self, __value: object) -> bool:
        return self.value == __value.value


class PhoneList:

    def __init__(self) -> None:
        self.phones = []

    def add_phone(self, phone: Phone) -> None:
        if phone in self.phones:
            return f'{phone} in PhoneList'
        self.phones.append(phone)
        return f"{phone} add to Phonelist"
    

if __name__ == '__main__':
    pl = PhoneList()

    p1 = Phone('12345')
    p2 = Phone('6789')
    p3 = Phone('12345')

    print(pl.add_phone(p1))
    print(pl.add_phone(p2))
    print(pl.add_phone(p3))

    print(pl.phones)
