
class Complex:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + i{self.image}'
    
    def __repr__(self):
        return f'{self.real} - i{self.image}'
    

number = Complex(10, 20)    

print(number)   # 10 + i20

print(str(number), repr(number))    # 10 + i20 10 - i20