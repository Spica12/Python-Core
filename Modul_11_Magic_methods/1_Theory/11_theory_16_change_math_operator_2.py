
class Adder:

    def __add__(self, obj):
        raise NotImplemented
    

class list_Adder(Adder):

    def __init__(self, value):
        self.value = value
    
    def __add__(self, obj):
        return self.value + obj.value
    

class Dist_Adder(Adder):

    def __init__(self, value):
        self.value = value
    
    def __add__(self, obj):
        return {**self.value, **obj.value}
    


list_adder = list_Adder([1, 2])
list_adder2 = list_Adder([3, 4])
print(list_adder + list_adder2)     # [1, 2, 3, 4]

dist_adder_one = Dist_Adder({1: 'a', 2: 'b'})
dist_adder_two = Dist_Adder({3: 'c', 4: 'd'})

print(dist_adder_one + dist_adder_two)     # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

