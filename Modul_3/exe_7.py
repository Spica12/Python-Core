"""
Наступне завдання буде суто теоретичним, і ми потренуємося 
працювати з довільною кількістю аргументів.

Створіть дві функції:

перша first буде мати першим параметром змінну size, а також вона 
може приймати будь-яку кількість позиційних аргументів. Функція 
повинна повернути суму size із загальною кількістю переданих до 
неї позиційних аргументів.

друга функція second так само матиме першим параметром size і 
прийматиме довільну кількість ключових аргументів, і також має 
повернути суму size з кількістю переданих у функцію ключових 
аргументів.

Тестові виклики функцій для правильності роботи будуть наступними:
- first(5, "first", "second", "third")
- first(1, "Alex", "Boris")
- second(3, comment_one="first", comment_two="second", 
  comment_third="third")
- second(10, comment_one="Alex", comment_two="Boris")
"""
# def first(size, ):
# 
# 
# 
# def second(size, ):
# ------------------------------------------------------
def first(size, *args):

    return size + len(args)    


def second(size, **args):

    return size + len(args)

first(5, "first", "second", "third")

first(1, "Alex", "Boris")

second(3, 
       comment_one="first", 
       comment_two="second",
       comment_third="third")

second(10, comment_one="Alex", comment_two="Boris")