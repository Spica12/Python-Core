"""
Для екземпляра класу Vector реалізуйте функтор. Створіть для класу 
Vector метод __call__. Він має реалізувати наступну поведінку:

vector = Vector(Point(1, 10))

print(vector())  # (1, 10)
При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.

Якщо при виклику ми передаємо параметр число, ми виконуємо добуток вектора 
на число — множимо кожну координату на вказане число та повертаємо кортеж з 
новими координатами вектора.

vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)
"""

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):

        if value is None:
            value = 1

        return (self.coordinates.x * value, self.coordinates.y * value)
            
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})" 
    

vector = Vector(Point(1, 10))
print(vector())
print(vector(5))