

class Iterator:

    def __init__(self):
        self.start = 7


    def __next__(self):
        self.start += 1
        if self.start >= 100:
            raise StopIteration
        return self.start
    
    def __iter__(self):
        self.start = 7
        return self    
    

my_iterator = Iterator()

for i in my_iterator:
    print(i)

print('-----')

for i in my_iterator:
    print(i)

print('-----')

for i in my_iterator:
    print(i)
