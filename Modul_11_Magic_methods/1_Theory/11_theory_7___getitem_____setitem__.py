from collections import UserList

class PositiveNumber(UserList):

    def __init__(self, data=[]):
        self.data = data

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        
        return self.data[idx]
    
    def __setitem__(self, key, value):
        if value > 0:
            self.data.append(value)


number = PositiveNumber()

number[0] = 1
print(number)   # [1]

number[1] = -3
number[2] = 5 

print(number)   # [1, 5]
print(number[1])    # 5
