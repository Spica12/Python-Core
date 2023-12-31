"""
Однією з класичних задач на розуміння рекурсії, яку часто задають 
на співбесідах, особливо початківцям-програмістам — це ряд 
Фібоначчі.

Ряд Фібоначчі — це послідовність чисел виду: 
0, 1, 1, 2, 3, 5, 8, ... де кожне наступне число послідовності 
виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі 
слід обчислити вираз:

Fn = Fn-1 + Fn-2.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що 
обчислює числа послідовності доти, доки виклик не сягне членів 
ряду менше n = 1, на якій задана послідовність.
"""
# def fibonacci(n):
# --------------------------------------------------------------
# fib(7) = fib(6) + fib(5)  --> fib(7) = 8 + 5  --> 13
# fib(6) = fib(5) + fib(4)  --> fib(6) = 5 + 3  --> 8
# fib(5) = fib(4) + fib(3)  --> fib(5) = 3 + 2  --> 5
# fib(4) = fib(3) + fib(2)  --> fib(4) = 2 + 1  --> 3
# fib(3) = fib(2) + fib(1)  --> fib(3) = 1 + 1  --> 2
# fib(2) = fib(1)           --> fib(2) = 1      --> 1
# fib(1) = 1                --> fib(1) = 1      --> 1



def fibonacci(n):

    if n == 0:
        return 0
    elif n <= 1:
        return 1    
    else:        
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(5))