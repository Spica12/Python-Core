

def func(f):
    f()


func(lambda: print('Hello'))        # Hello


some_list = [(lambda i: i ** 2)(i) for i in range(10)]
print(some_list)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]