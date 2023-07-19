"""
Факторіал це функція, визначена на множині додатних цілих чисел.
n! = 1 · 2 · ... · n

0! = 1
"""


'''
10! = 9! * 10
9! = 8! * 9
8! = 7! * 8
...
1! = 0! * 1
0! = 1
'''

def factorial(n):

    if n < 2: # Я використовував n == 0
        return 1 # Базовий параметр

    return factorial(n-1) * n # Рекурсивний випадок

    

# 1*2*3*4*5*6*7*8*9*10 = 3 628 800
number = factorial(10)
print(number)

number = int(input('Enter positive integer number: '))
result = factorial(number)
print(f'Факторіал числа {number} дорівнює {result}')