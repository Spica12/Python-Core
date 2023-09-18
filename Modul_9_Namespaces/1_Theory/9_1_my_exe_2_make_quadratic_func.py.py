def make_quadratic(a, b, c):

    def quadratic(x):
        return a*x*x + b*x + c
    
    return quadratic


f1 = make_quadratic(1, 0, 0)
print(f1(5))    # 5 is x
print(f1(7))
print(f1(9))
print(f1(10))

f2 = make_quadratic(2, 2, 2)
print(f2(5))
print(f2(7))
print(f2(9))
print(f2(10))

print(id(f1) == id(f2))