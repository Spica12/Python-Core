

class MyIterator:

    def __init__(self, seq, stop):
        self.seq = seq
        self.stop = stop
        self.loop = 0
        self.idx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.loop >= self.stop:
            raise StopIteration
        else:
            value = self.seq[self.idx]
            self.idx += 1
            if self.idx == len(self.seq):
                self.idx = 0
                self.loop += 1

            return value
        

seq = ['q', 'w', 'e', 1, 2, 3, 4, 5]

my_iterator = MyIterator(seq, 2)

for val in my_iterator:
    print(val)

# q
# w
# e
# 1
# 2
# 3
# 4
# 5
# q
# w
# e
# 1
# 2
# 3
# 4
# 5