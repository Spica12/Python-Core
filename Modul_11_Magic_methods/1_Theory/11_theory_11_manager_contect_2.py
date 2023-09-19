from datetime import datetime, timedelta
from time import sleep

class FileReader:

    def __init__(self, filename):
        self.file = None
        self.opened = None
        self.log = ''
        self.tstmp = None
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.tstmp = datetime.now().timestamp()
        msg = '{:<20}|{:^15}|\n'.format(self.tstmp, self.filename)
        self.log += msg

        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            tstmp = datetime.now().timestamp()
            diff = tstmp - self.tstmp
            msg = '{:<20}|{:^15}|{:>4.0f}\n'.format(self.tstmp, self.filename, diff)
            self.log += msg
        self.opened = False
        if exc_val is not None:
            print('Oh No!')


reader = FileReader('11_theory_9_some.txt')

with reader as f:
    print(f.read())

with reader as f:
    sleep(2)
    print(f.read())

print(reader.log)