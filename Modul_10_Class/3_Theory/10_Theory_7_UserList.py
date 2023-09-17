from collections import UserList
from random import randint


class ExperimentsResult(UserList):

    def positive_values(self):
        return list(filter(lambda x: x > 0, self.data))
                    
    def negative_values(self):
        return list(filter(lambda x: x < 0, self.data))
                    

result = ExperimentsResult()

for _ in range(0, 20):
    result.append(randint(-5, 5))


print(result)
print(result.negative_values())
print(result.positive_values())