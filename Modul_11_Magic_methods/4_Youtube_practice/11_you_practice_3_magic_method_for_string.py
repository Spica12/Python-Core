class str(str):

    def __add__(self, other):
        return 1
    

a = str('a')
b = str('b')
c = 'c'

print(type(a))  # <class '__main__.str'>
print(type(b))  # <class '__main__.str'>       - визначенний користувацький з модуля main
print(type(c))  # <class 'str'>                - вбудований python 

print(a + b)    # 1