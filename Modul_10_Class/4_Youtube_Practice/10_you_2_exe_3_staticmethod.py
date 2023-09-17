class A:

    @staticmethod                           # Метод без передачі self
    def method():
        print('asd')



a = A()
a.method()      # asd

A.method()      # asd