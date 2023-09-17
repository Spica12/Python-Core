

def adder(value):

    def inner(number):
        return value + number
    
    return inner

two_adder = adder(2)
print(two_adder(3), two_adder(5))

print((adder(3)(8)))
