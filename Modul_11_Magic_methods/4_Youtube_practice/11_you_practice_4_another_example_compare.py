class str(str):


    def __add__(self, other):
        return 1
    
    def __eq__(self, other):
        if isinstance(other, int):
            print(self, other.__str__())
            return super().__eq__(other.__str__())
        
a = str('1')
b = 1

print(a == b)