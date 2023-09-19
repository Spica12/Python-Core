"""
__getitem__
__setitem__

Коли ви хочете отримати значення, використовуючи квадратні дужки, в 
об'єкта викликається метод __getitem__.
Для запису значення з індексом або ключем викликається метод __setitem__. 
Обидва ці методи приймають першим аргументом self. __getitem__ другим 
аргументом приймає індекс або ключ, за яким потрібно знайти елемент, а 
__setitem__ другим аргументом приймає ключ/індекс, а третім значення, 
яке потрібно записати за цим ключем/індексом.
"""

class ListedValuesDict:

    def __init__(self):
        self.data = dict()

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ', ' + str(value)
        return result
    

l_dict = ListedValuesDict()

l_dict[1] = 'a'
l_dict[1] = 'b'

print(l_dict[1])    # a, b
