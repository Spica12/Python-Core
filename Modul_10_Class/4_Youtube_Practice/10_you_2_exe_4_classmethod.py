class A:

    @classmethod                           # Метод без передачі self
    def method(class_):
        print(class_)                       # Зробити не класовий метод класовим
                                    
# Необхідно ставити class_


a = A()
a.method()      # asd

A.method()      # asd


print(help(classmethod))