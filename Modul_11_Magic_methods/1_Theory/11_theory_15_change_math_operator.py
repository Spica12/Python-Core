
class Adder:

    def __add__(self, obj):
        raise NotImplemented
    

class list_Adder(Adder):

    def __init__(self, value):
        self.value = value
    
    def __add__(self, obj):
        return self.value + obj.value
    


adder = Adder()
another_adder = Adder()

try:
    print(adder + another_adder)
except:
    print('Error')

list_adder = list_Adder([1, 2])
list_adder2 = list_Adder([3, 4])
print(list_adder + list_adder2)     # [1, 2, 3, 4]


