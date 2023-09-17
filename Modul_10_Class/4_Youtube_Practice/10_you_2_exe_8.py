class Record:

    def __init__(self, name):
        self.name = name


class Name:
    value = 'ASD'


record = Record(Name())
print(record.name.value)