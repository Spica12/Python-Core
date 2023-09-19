
#  __enter__
#  __exit__

class FileWritter:

    def __init__(self, filename):
        self.file = None
        self.opened = None
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
        if exc_val is not None:
            print('Something wrong')


with FileWritter('11_theory_9_some.txt') as file:
    file.write('Hello!\n')