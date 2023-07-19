print('----------- Example 1 ----------')

x = 50

def func():

    global x
    print('Function: x equal', x) # x equal 50

    x = 2
    print('Function: Change global x to ', x) # Change global x to 2

func()
print('Global: Value x equal', x)