
class SomeDict:

    def __init__(self):
        self.data = dict()

    def __setitem__(self, key, item):
        self.data[key] = item

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None
        

my_dict = SomeDict()
my_dict[0] = 'Hello'
my_dict[1] = 'World'

get_from_zero = my_dict[0]
get_from_first = my_dict[1]
get_from_second = my_dict[2]

print(get_from_zero, get_from_first, get_from_second)   # Hello World None