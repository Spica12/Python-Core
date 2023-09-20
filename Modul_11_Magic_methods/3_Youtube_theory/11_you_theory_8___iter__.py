for i in range(10):
    print(i)


# Тільки ітеруємиє об'єкти

class Iterator:

    def __init__(self):
        self.start = 7


    def __next__(self):
        self.start += 1
        if self.start == 100:
            raise StopIteration
        return self.start



class MyIterator:

    def __iter__(self):
        return Iterator()

my_iterator = MyIterator()

for i in my_iterator:
    print(i)



# iter() returned non-iterator of type 'NoneType'