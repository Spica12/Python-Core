# Closure Замикання

def average():

    values = []

    def inner(value:int)->float:
        values.append(value)
        return sum(values) / len(values)
    
    return inner


if __name__ == '__main__':

    avg = average()

    print(avg(10))
    print(avg(20))
    print(avg(30))
    print(avg(40))
    print(avg(50))
    print(avg(60))


