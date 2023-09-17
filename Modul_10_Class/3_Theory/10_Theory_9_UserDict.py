from collections import UserDict


class DualDict(UserDict):

    def __init__(self, initial=None):

        if initial is None:
            self.from_value = {}
            self.data = {}
        else:
            self.data = initial
            self.from_value = {val:key for key, val in initial.items()}


    def __setitem__(self, key, value):

        self.data[key] = value

        if value in self.from_value:
            old = self.from_value[value]
            self.from_value.pop(old)

        self.from_value[value] = key

    def get_by_value(self, value):
        return self.from_value(value)


    def set_by_value(self, value, key):

        old_key = self.from_value[value]
        self.data.pop(old_key)
        self.data[key] = value
        self.from_value[value] = key


dual = DualDict({1:2, 3:4})
print(dual)
print(dual.get_by_value(2) == 2)