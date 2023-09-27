num1 = 10
num2 = 0

result = None
try:
    sult = num1 / num2
except ZeroDivisionError:
    print('You can\'t divide by zero')

if not result:
    print('Not operation')
